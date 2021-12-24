"""This module contains implementations of 'stack' data structure"""
import operator
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional, Callable, Tuple

Item = TypeVar('Item')


class AbstractStack(ABC, Generic[Item]):

    @abstractmethod
    def push(self, item: Item) -> None:
        pass

    @abstractmethod
    def pop(self) -> Item:
        pass

    @abstractmethod
    def peek(self) -> Item:
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

    def peek(self) -> Item:
        return self.__data[-1]

    def pop(self) -> Item:
        return self.__data.pop()

    def is_empty(self) -> bool:
        return not self.__data

    def as_list(self) -> List[Item]:
        return self.__data[:]

    def __len__(self) -> int:
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
            maximum = self.__maximums.peek()
            if item > maximum:
                self.__maximums.push(item)
            else:
                self.__maximums.push(maximum)

    def pop(self) -> int:
        self.__maximums.pop()
        return self.__stack.pop()

    def peek(self) -> int:
        return self.__stack.peek()

    def maximum(self) -> Optional[int]:
        return self.__maximums.peek()

    def is_empty(self) -> bool:
        return self.__stack.is_empty()

    def as_list(self) -> List[Item]:
        return self.__stack.as_list()


class ComparableStack(AbstractStack[Optional[Item]]):
    def __init__(self, comparison_operator: Callable[[Item, Item], bool]):
        self.__stack: Stack[Optional[Item]] = Stack[Optional[Item]]()
        self.__comparison_operator: Callable[[Item, Item], bool] = comparison_operator

    def push(self, item: Optional[Item]) -> None:
        self.__push(item, False)

    def pop_and_push(self, item: Optional[Item]) -> None:
        self.__push(item, True)

    def __push(self, item: Optional[Item], pop: bool) -> None:
        if not self.__stack.is_empty():
            last = self.__last(pop)
            if last is not None and (item is None or self.__comparison_operator(item, last)):
                self.__stack.push(last)
            else:
                self.__stack.push(item)
        else:
            self.__stack.push(item)

    def __last(self, pop: bool) -> Optional[Item]:
        return self.__stack.pop() if pop else self.__stack.peek()

    def pop(self) -> Optional[Item]:
        return self.__stack.pop()

    def peek(self) -> Optional[Item]:
        return self.__stack.peek()

    def is_empty(self) -> bool:
        return self.__stack.is_empty()

    def as_list(self) -> List[Optional[Item]]:
        return self.__stack.as_list()

    def __len__(self) -> int:
        return len(self.__stack)


class MinMaxStack(AbstractStack[Tuple[Optional[Item], Optional[Item]]]):
    def __init__(self):
        self.__min_stack: ComparableStack[Item] = ComparableStack[Item](operator.lt)
        self.__max_stack: ComparableStack[Item] = ComparableStack[Item](operator.gt)

    def push(self, item: Tuple[Optional[Item], Optional[Item]]) -> None:
        minimum, maximum = item
        self.__min_stack.push(minimum)
        self.__max_stack.push(maximum)

    def pop_and_push(self, item: Tuple[Optional[Item], Optional[Item]]) -> None:
        minimum, maximum = item
        self.__min_stack.pop_and_push(minimum)
        self.__max_stack.pop_and_push(maximum)

    def pop(self) -> Tuple[Optional[Item], Optional[Item]]:
        return self.__min_stack.pop(), self.__max_stack.pop()

    def peek(self) -> Tuple[Optional[Item], Optional[Item]]:
        return self.__min_stack.peek(), self.__max_stack.peek()

    def is_empty(self) -> bool:
        return self.__min_stack.is_empty() and self.__max_stack.is_empty()

    def as_list(self) -> List[Tuple[Optional[Item], Optional[Item]]]:
        minimums = self.__min_stack.as_list()
        maximums = self.__max_stack.as_list()
        items = []
        for i, minimum in enumerate(minimums):
            items.append((minimum, maximums[i]))
        return items

    def __len__(self) -> int:
        return len(self.__min_stack)
