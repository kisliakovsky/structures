"""This module contains implementations of 'disjoint set' data structure"""

from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic, Tuple

Value = TypeVar('Value')


class AbstractDisjointSet(ABC, Generic[Value]):

    @abstractmethod
    def make_set(self, i: int, value: Value) -> None:
        pass

    @abstractmethod
    def find(self, i: int) -> int:
        pass

    @abstractmethod
    def union(self, i: int, j: int) -> None:
        pass

    @abstractmethod
    def as_list(self) -> List[Tuple[int, Value]]:
        pass


class DisjointSet(AbstractDisjointSet[Value]):
    def __init__(self, size: int):
        self.__size = size
        self.__parents: List[Optional[int]] = [None for _ in range(size)]
        self.__ranks: List[Optional[int]] = [None for _ in range(size)]
        self.__values: List[Optional[Value]] = [None for _ in range(size)]

    def make_set(self, i: int, value: Value) -> None:
        if i >= self.__size:
            raise IndexError("index out of range")
        if self.__parents[i] is not None:
            raise ValueError("set already made")
        self.__parents[i] = i
        self.__values[i] = value
        self.__ranks[i] = 1

    def find(self, i: int) -> int:
        if i >= self.__size:
            raise IndexError("index out of range")
        return self.__find(i)

    def __find(self, i: int) -> int:
        parent = self.__parents[i]
        if parent is None:
            raise ValueError("item does not exist")
        if i != parent:
            parent = self.__find(self.__parents[i])
            self.__parents[i] = parent
        return self.__parents[i]

    def union(self, i: int, j: int) -> None:
        if i >= self.__size or j >= self.__size:
            raise IndexError("index out of range")
        i_root = self.__find(i)
        j_root = self.__find(j)
        if i_root is None or j_root is None:
            raise ValueError("items do not exist")
        i_rank = self.__ranks[i_root]
        j_rank = self.__ranks[j_root]
        if i_rank > j_rank:
            self.__parents[i_root] = j_root
        else:
            self.__parents[j_root] = i_root
            if i_rank == j_rank:
                self.__ranks[j_root] += 1

    def as_list(self) -> List[Tuple[int, Value]]:
        return self.__as_list()

    def __as_list(self) -> List[Tuple[int, Value]]:
        return [(self.__values[i], self.__find(i)) for i in range(self.__size)]

    def __str__(self):
        return str(self.__as_list())


class DisjointSetWithMaxSum(AbstractDisjointSet[int]):
    def __init__(self, size: int):
        self.__disjoint_set: DisjointSet[int] = DisjointSet[int](size)
        self.__values: List[Optional[int]] = [None for _ in range(size)]
        self.__max_root: Optional[int] = None

    def make_set(self, i: int, value: int) -> None:
        self.__disjoint_set.make_set(i, value)
        self.__values[i] = value
        if self.__max_root is None or self.__values[self.__max_root] < value:
            self.__max_root = i

    def find(self, i: int) -> int:
        return self.__disjoint_set.find(i)

    def union(self, i: int, j: int) -> None:
        if i != j:
            i_root = self.__disjoint_set.find(i)
            j_root = self.__disjoint_set.find(j)
            if i_root != j_root:
                self.__values[i_root] += self.__values[j_root]
                self.__values[j_root] = 0
                if self.__max_root == j_root:
                    self.__max_root = i_root
                elif self.__max_root != i_root:
                    if self.__values[self.__max_root] < self.__values[i_root]:
                        self.__max_root = i_root
                self.__disjoint_set.union(i, j)

    def max_sum(self) -> Optional[int]:
        return self.__values[self.__max_root]

    def as_list(self) -> List[Tuple[int, int]]:
        return self.__disjoint_set.as_list()
