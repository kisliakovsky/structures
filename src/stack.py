from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

T = TypeVar('T')


class AbstractStack(ABC, Generic[T]):

    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> Optional[T]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def as_list(self) -> List[T]:
        pass


class Stack(AbstractStack[T]):
    def __init__(self) -> None:
        self.__data: List[T] = []

    def push(self, item: T) -> None:
        self.__data.append(item)

    def peak(self) -> Optional[T]:
        return self.__data[-1] if self.__data else None

    def pop(self) -> Optional[T]:
        return self.__data.pop() if self.__data else None

    def is_empty(self) -> bool:
        return not self.__data

    def as_list(self) -> List[T]:
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

    def pop(self) -> Optional[int]:
        self.__maximums.pop()
        return self.__stack.pop()

    def maximum(self) -> Optional[int]:
        return self.__maximums.peak()

    def is_empty(self) -> bool:
        return self.__stack.is_empty()

    def as_list(self) -> List[T]:
        return self.__stack.as_list()
