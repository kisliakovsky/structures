"""This module contains implementations of 'heap' data structure"""

from abc import ABC, abstractmethod, ABCMeta
from typing import TypeVar, Generic, List, Iterator

GenericKey = TypeVar('GenericKey', bound='Key')
Value = TypeVar('Value')
GenericHeapNode = TypeVar('GenericHeapNode', bound='HeapNode')


class Key(Generic[GenericKey], metaclass=ABCMeta):

    @abstractmethod
    def compare_to(self, other: 'Key') -> int:
        pass

    @abstractmethod
    def more(self) -> GenericKey:
        pass


class MinIntKey(Key['MinIntKey']):
    def __init__(self, value: int):
        self.__value = value

    def compare_to(self, other: 'MinIntKey') -> int:
        return other.__value - self.__value

    def more(self) -> 'MinIntKey':
        return MinIntKey(self.__value - 1)

    def __eq__(self, other: 'MinIntKey'):
        return self.__value == other.__value if isinstance(other, MinIntKey) else False

    def __str__(self):
        return str(self.__value)


class MaxIntKey(Key['MaxIntKey']):
    def __init__(self, value: int):
        self.__value = value

    def compare_to(self, other: 'MaxIntKey') -> int:
        return self.__value - other.__value

    def more(self) -> 'MaxIntKey':
        return MaxIntKey(self.__value + 1)

    def __eq__(self, other: 'MaxIntKey'):
        return self.__value == other.__value if isinstance(other, MaxIntKey) else False

    def __str__(self):
        return str(self.__value)


class HeapNode(ABC, Generic[GenericKey, Value, GenericHeapNode]):

    @abstractmethod
    def key(self) -> GenericKey:
        pass

    @abstractmethod
    def value(self) -> Value:
        pass

    @abstractmethod
    def copy(self, key: GenericKey) -> GenericHeapNode:
        pass


class Entry(HeapNode[GenericKey, Value, 'Entry']):
    def __init__(self, key: GenericKey, value: Value):
        self.__key = key
        self.__value = value

    def key(self) -> GenericKey:
        return self.__key

    def value(self) -> Value:
        return self.__value

    def copy(self, key: GenericKey) -> GenericHeapNode:
        return Entry(key, self.__value)

    def __eq__(self, other: 'Entry'):
        if isinstance(other, Entry):
            return self.__key == other.__key and self.__value == other.__value
        return False

    def __str__(self):
        return f"[{self.__key}, {self.__value}]"


class Unit(HeapNode[GenericKey, GenericKey, 'Unit']):
    def __init__(self, key: GenericKey):
        self.__key = key

    def key(self) -> GenericKey:
        return self.__key

    def value(self) -> GenericKey:
        return self.__key

    def copy(self, key: GenericKey) -> GenericHeapNode:
        return Unit(self.__key)

    def __eq__(self, other: 'Unit'):
        return self.__key == other.__key if isinstance(other, Unit) else False

    def __str__(self):
        return str({self.__key})


class Heap(Generic[GenericKey, Value], ABC):
    def __init__(self, num_of_children, data: List[HeapNode[GenericKey, Value, GenericHeapNode]]):
        if num_of_children < 2:
            raise ValueError("Number of children must be greater than 1")
        self.__number_of_children = num_of_children
        self.__data: List[HeapNode[GenericKey, Value, GenericHeapNode]] = data
        for i in range(len(data) // self.__number_of_children - 1, -1, -1):
            self.__sift_down(i)

    def push(self, item: HeapNode[GenericKey, Value, GenericHeapNode]) -> None:
        self.__data.append(item)
        self.__sift_up(len(self.__data) - 1)

    def pop(self) -> HeapNode[GenericKey, Value, GenericHeapNode]:
        return self.__pop()

    def peak(self) -> HeapNode[GenericKey, Value, GenericHeapNode]:
        return self.__data[0]

    def change_key(self, i: int, key: GenericKey) -> None:
        if i < len(self.__data):
            item_key = self.__data[i].key()
            self.__data[i] = self.__data[i].copy(key)
            if self.__data[i].key().compare_to(item_key) > 0:
                self.__sift_up(i)
            else:
                self.__sift_down(i)
        else:
            raise IndexError("index out of range")

    def __delitem__(self, i: int):
        if i < len(self.__data):
            root = self.__data[0]
            self.__data[i] = root.copy(root.key().more())
            self.__sift_up(i)
            self.__pop()
        else:
            raise IndexError("index out of range")

    def as_list(self) -> List[HeapNode[GenericKey, Value, GenericHeapNode]]:
        return self.__data[:]

    def is_empty(self) -> bool:
        return not self.__data

    def __pop(self) -> HeapNode[GenericKey, Value, GenericHeapNode]:
        last = self.__data.pop()
        if self.__data:
            result = self.__data[0]
            self.__data[0] = last
            self.__sift_down(0)
            return result
        return last

    def __sift_up(self, i: int) -> None:
        while self.__data[self.__parent_i(i)].key().compare_to(self.__data[i].key()) < 0 < i:
            parent_i = self.__parent_i(i)
            self.__swap(parent_i, i)
            i = parent_i

    def __sift_down(self, i: int) -> None:
        extreme_i = None
        while extreme_i != i:
            extreme_i = i
            for child_i in self.__children_i(i):
                if self.__data[child_i].key().compare_to(self.__data[extreme_i].key()) > 0:
                    extreme_i = child_i
            if i != extreme_i:
                self.__swap(i, extreme_i)
                i = extreme_i
                extreme_i = None

    def __swap(self, i: int, j: int) -> None:
        self.__data[i], self.__data[j] = self.__data[j], self.__data[i]

    def __children_i(self, parent_i: int) -> Iterator[int]:
        size = len(self.__data)
        for i in range(0, self.__number_of_children):
            child_i = self.__number_of_children * parent_i + i + 1
            if child_i < size:
                yield child_i

    def __parent_i(self, child_i: int) -> int:
        return (child_i - 1) // self.__number_of_children


class FasterMinHeap:
    def __init__(self, data):
        self.__data = data
        for i in range(len(data) // 2 - 1, -1, -1):
            self.__sift_down(i)

    def push(self, item):
        self.__data.append(item)
        self.__sift_up(len(self.__data) - 1)

    def pop(self):
        last = self.__data.pop() if self.__data else None
        if self.__data:
            result = self.__data[0]
            self.__data[0] = last
            self.__sift_down(0)
            return result
        return last

    def peak(self):
        return self.__data[0] if self.__data else None

    def change_key(self, i, value):
        if i < len(self.__data):
            item = self.__data[i]
            self.__data[i] = value
            if value < item:
                self.__sift_up(i)
            else:
                self.__sift_down(i)
        else:
            raise IndexError("index out of range")

    def as_list(self):
        return self.__data[:]

    def is_empty(self):
        return not self.__data

    def __sift_up(self, i):
        while i > 0 and self.__data[self.__parent_i(i)] > self.__data[i]:
            parent_i = self.__parent_i(i)
            self.__swap(parent_i, i)
            i = parent_i

    def __sift_down(self, i):
        extreme_i = None
        while extreme_i != i:
            extreme_i = i
            for child_i in self.__children_i(i):
                if self.__data[child_i] < self.__data[extreme_i]:
                    extreme_i = child_i
            if i != extreme_i:
                self.__swap(i, extreme_i)
                i = extreme_i
                extreme_i = None

    def __swap(self, i, j):
        self.__data[i], self.__data[j] = self.__data[j], self.__data[i]

    def __children_i(self, parent_i):
        size = len(self.__data)
        for i in range(0, 2):
            child_i = 2 * parent_i + i + 1
            if child_i < size:
                yield child_i

    @staticmethod
    def __parent_i(child_i):
        return (child_i - 1) >> 1
