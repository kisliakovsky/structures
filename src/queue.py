from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

from src.stack import Stack, StackWithMaxValue

T = TypeVar('T')


class AbstractQueue(ABC, Generic[T]):

    @abstractmethod
    def enqueue(self, item: T) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Optional[T]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def as_list(self) -> List[T]:
        pass


class AbstractQueueWithMaxValue(AbstractQueue[int]):

    @abstractmethod
    def maximum(self) -> Optional[int]:
        pass


class Queue(AbstractQueue[T]):
    def __init__(self) -> None:
        self.__data: List[T] = []

    def enqueue(self, item: T) -> None:
        self.__data.append(item)

    def dequeue(self) -> Optional[T]:
        if self.__data:
            item = self.__data[0]
            del self.__data[0]
            return item
        else:
            return None

    def peak(self) -> Optional[T]:
        return self.__data[0] if self.__data else None

    def is_empty(self) -> bool:
        return not self.__data

    def as_list(self) -> List[T]:
        copy = self.__data[:]
        copy.reverse()
        return copy


class QueueWithMaxValue(AbstractQueueWithMaxValue):
    def __init__(self):
        self.__queue: Queue[int] = Queue[int]()
        self.__prev_item: Optional[int] = None
        self.__maximums: Queue[int] = Queue[int]()

    def enqueue(self, item: int) -> None:
        if self.__prev_item is not None and self.__prev_item < item:
            maximums = Queue[int]()
            while not self.__maximums.is_empty():
                maximum = self.__maximums.dequeue()
                if maximum >= item:
                    maximums.enqueue(maximum)
            self.__maximums = maximums
        self.__maximums.enqueue(item)
        self.__prev_item = item
        self.__queue.enqueue(item)

    def dequeue(self) -> Optional[int]:
        item = self.__queue.dequeue()
        if item == self.__maximums.peak():
            self.__maximums.dequeue()
        return item

    def maximum(self) -> Optional[int]:
        return self.__maximums.peak()

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

    def dequeue(self) -> Optional[int]:
        if self.__dequeue_stack.is_empty():
            while not self.__enqueue_stack.is_empty():
                self.__dequeue_stack.push(self.__enqueue_stack.pop())
            self.__enqueue_stack_max = None
        return self.__dequeue_stack.pop()

    def maximum(self) -> Optional[int]:
        if self.__enqueue_stack.is_empty():
            if self.__dequeue_stack.is_empty():
                return None
            else:
                return self.__dequeue_stack.maximum()
        else:
            if self.__dequeue_stack.is_empty():
                return self.__enqueue_stack_max
            else:
                return max(self.__enqueue_stack_max, self.__dequeue_stack.maximum())

    def is_empty(self) -> bool:
        return self.__enqueue_stack.is_empty() and self.__dequeue_stack.is_empty()

    def as_list(self) -> List[int]:
        dequeue_copy = self.__dequeue_stack.as_list()[:]
        enqueue_copy = self.__enqueue_stack.as_list()[:]
        enqueue_copy.reverse()
        return dequeue_copy + enqueue_copy
