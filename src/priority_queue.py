from typing import Generic, TypeVar, List, Optional

from src.binary_heap import HeapNode, BinaryMaxHeap, BinaryHeap
from src.queue import AbstractQueue

T = TypeVar('T')


class PrioritizedItem(Generic[T]):
    def __init__(self, priority: int, value: T):
        self.__priority = priority
        self.__value = value

    def priority(self) -> int:
        return self.__priority

    def value(self) -> T:
        return self.__value

    def as_heap_node(self) -> HeapNode[T]:
        return HeapNode(self.__priority, self.__value)

    def __eq__(self, other):
        if isinstance(other, PrioritizedItem):
            return self.__priority == other.__priority and self.__value == other.__value
        else:
            return False

    def __str__(self):
        return f"[{self.__priority}, {self.__value}]"

    @staticmethod
    def prioritized_item(heap_node: HeapNode[T]):
        return PrioritizedItem(heap_node.key(), heap_node.value())


class PriorityQueue(AbstractQueue[PrioritizedItem[T]]):
    def __init__(self, heap: BinaryHeap[T]):
        self.__heap = heap

    def enqueue(self, item: PrioritizedItem[T]) -> None:
        self.__heap.push(item.as_heap_node())

    def dequeue(self) -> Optional[PrioritizedItem[T]]:
        return PrioritizedItem.prioritized_item(self.__heap.pop())

    def peak(self) -> Optional[PrioritizedItem[T]]:
        return PrioritizedItem.prioritized_item(self.__heap.peak())

    def change_priority(self, i: int, priority: int):
        self.__heap.change_key(i, priority)

    def __delitem__(self, i: int):
        del self.__heap[i]

    def is_empty(self) -> bool:
        return self.__heap.is_empty()

    def as_list(self) -> List[PrioritizedItem[T]]:
        return list(map(PrioritizedItem.prioritized_item, self.__heap.as_list()))
