"""This module contains implementations of 'stack' data structure"""

from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

Item = TypeVar('Item')


class AbstractStack(ABC, Generic[Item]):

    @abstractmethod
    def push(self, item: Item) -> None:
        pass

    @abstractmethod
    def pop(self) -> Item:
        pass

    @abstractmethod
    def peak(self) -> Item:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def as_list(self) -> List[Item]:
        pass


class Stack(AbstractStack[Item]):
    def __init__(self) -> None:
        self.__data: List[Item] = []

    def push(self, item: Item) -> None:
        self.__data.append(item)

    def peak(self) -> Item:
        return self.__data[-1]

    def pop(self) -> Item:
        return self.__data.pop()

    def is_empty(self) -> bool:
        return not self.__data

    def as_list(self) -> List[Item]:
        return self.__data[:]

    def __len__(self):
        return len(self.__data)


class StackWithMaxValue(AbstractStack[int]):
    def __init__(self):
        self.__stack: Stack[int] = Stack[int]()
        self.__maximums: Stack[int] = Stack[int]()

    def push(self, item: int) -> None:
        if self.__stack.is_empty():
            self.__stack.push(item)
            self.__maximums.push(item)
        else:
            self.__stack.push(item)
            maximum = self.__maximums.peak()
            if item > maximum:
                self.__maximums.push(item)
            else:
                self.__maximums.push(maximum)

    def pop(self) -> int:
        self.__maximums.pop()
        return self.__stack.pop()

    def peak(self) -> int:
        return self.__stack.peak()

    def maximum(self) -> Optional[int]:
        return self.__maximums.peak()

    def is_empty(self) -> bool:
        return self.__stack.is_empty()

    def as_list(self) -> List[Item]:
        return self.__stack.as_list()
