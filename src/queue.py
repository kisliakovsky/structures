from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

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
        copy = self.__data.copy()
        copy.reverse()
        return copy


class QueueWithMaxValue(AbstractQueue[int]):
    def __init__(self):
        self.__queue: Queue[int] = Queue[int]()
        self.__maximums: Queue[int] = Queue[int]()

    def enqueue(self, item: T) -> None:
        maximums = Queue[int]()
        while not self.__maximums.is_empty():
            maximum = self.__maximums.dequeue()
            if maximum >= item:
                maximums.enqueue(maximum)
        maximums.enqueue(item)
        self.__maximums = maximums
        self.__queue.enqueue(item)

    def dequeue(self) -> Optional[T]:
        item = self.__queue.dequeue()
        if item == self.__maximums.peak():
            self.__maximums.dequeue()
        return item

    def max(self) -> Optional[T]:
        return self.__maximums.peak()

    def is_empty(self) -> bool:
        return self.__queue.is_empty()

    def as_list(self) -> List[T]:
        return self.__queue.as_list()
