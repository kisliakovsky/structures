"""This module contains implementations of 'queue' data structure"""

from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

from src.stack import Stack, StackWithMaxValue

Item = TypeVar('Item')


class AbstractQueue(ABC, Generic[Item]):

    @abstractmethod
    def enqueue(self, item: Item) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Item:
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


class AbstractQueueWithMaxValue(AbstractQueue[int]):

    @abstractmethod
    def maximum(self) -> Optional[int]:
        pass


class Queue(AbstractQueue[Item]):
    def __init__(self, data: List[Item]) -> None:
        self.__data: List[Item] = data

    def enqueue(self, item: Item) -> None:
        self.__data.append(item)

    def dequeue(self) -> Item:
        item = self.__data[0]
        del self.__data[0]
        return item

    def peek(self) -> Item:
        return self.__data[0]

    def is_empty(self) -> bool:
        return not self.__data

    def as_list(self) -> List[Item]:
        copy = self.__data[:]
        copy.reverse()
        return copy

    def __len__(self) -> int:
        return len(self.__data)

    def __eq__(self, other: 'Queue'):
        return self.__data == other.__data if isinstance(other, Queue) else False


class FullQueueError(Exception):
    pass


class LimitedQueue(AbstractQueue[Item]):

    def __init__(self, max_len: int):
        self.__queue = Queue[Item]([])
        self.__max_len = max_len

    def enqueue(self, item: Item) -> None:
        if len(self.__queue) < self.__max_len:
            self.__queue.enqueue(item)
        else:
            raise FullQueueError()

    def is_full(self) -> bool:
        return len(self.__queue) == self.__max_len

    def dequeue(self) -> Item:
        return self.__queue.dequeue()

    def peek(self) -> Item:
        return self.__queue.peek()

    def is_empty(self) -> bool:
        return self.__queue.is_empty()

    def as_list(self) -> List[Item]:
        return self.__queue.as_list()


class QueueWithMaxValue(AbstractQueueWithMaxValue):
    def __init__(self):
        self.__queue: Queue[int] = Queue[int]([])
        self.__prev_item: Optional[int] = None
        self.__maximums: Queue[int] = Queue[int]([])

    def enqueue(self, item: int) -> None:
        if self.__prev_item is not None and self.__prev_item < item:
            maximums = Queue[int]([])
            while not self.__maximums.is_empty():
                maximum = self.__maximums.dequeue()
                if maximum >= item:
                    maximums.enqueue(maximum)
            self.__maximums = maximums
        self.__maximums.enqueue(item)
        self.__prev_item = item
        self.__queue.enqueue(item)

    def dequeue(self) -> int:
        item = self.__queue.dequeue()
        if item == self.__maximums.peek():
            self.__maximums.dequeue()
        return item

    def maximum(self) -> Optional[int]:
        return self.__maximums.peek()

    def peek(self) -> Item:
        return self.__queue.peek()

    def is_empty(self) -> bool:
        return self.__queue.is_empty()

    def as_list(self) -> List[int]:
        return self.__queue.as_list()


class StackBasedQueueWithMaxValue(AbstractQueueWithMaxValue):
    def __init__(self):
        self.__enqueue_stack = Stack[int]()
        self.__enqueue_stack_max: Optional[int] = None
        self.__dequeue_stack = StackWithMaxValue()

    def enqueue(self, item: int) -> None:
        if self.__enqueue_stack_max is None or item > self.__enqueue_stack_max:
            self.__enqueue_stack_max = item
        self.__enqueue_stack.push(item)

    def dequeue(self) -> int:
        if self.__dequeue_stack.is_empty():
            while not self.__enqueue_stack.is_empty():
                self.__dequeue_stack.push(self.__enqueue_stack.pop())
            self.__enqueue_stack_max = None
        return self.__dequeue_stack.pop()

    def peek(self) -> Item:
        if self.__dequeue_stack.is_empty():
            while not self.__enqueue_stack.is_empty():
                self.__dequeue_stack.push(self.__enqueue_stack.pop())
            self.__enqueue_stack_max = None
        return self.__dequeue_stack.peek()

    def maximum(self) -> Optional[int]:
        if self.__enqueue_stack.is_empty():
            return None if self.__dequeue_stack.is_empty() else self.__dequeue_stack.maximum()
        if self.__dequeue_stack.is_empty():
            return self.__enqueue_stack_max
        return max(self.__enqueue_stack_max, self.__dequeue_stack.maximum())

    def is_empty(self) -> bool:
        return self.__enqueue_stack.is_empty() and self.__dequeue_stack.is_empty()

    def as_list(self) -> List[int]:
        dequeue_copy = self.__dequeue_stack.as_list()[:]
        enqueue_copy = self.__enqueue_stack.as_list()[:]
        enqueue_copy.reverse()
        return dequeue_copy + enqueue_copy
