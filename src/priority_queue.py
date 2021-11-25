from abc import ABC, ABCMeta
from typing import Generic, TypeVar, List, Optional

from src.binary_heap import HeapNode, BinaryHeap, Key, K
from src.queue import AbstractQueue

V = TypeVar('V')
P = TypeVar('P', bound='Priority')


class Priority(Key[P],  metaclass=ABCMeta):
    pass


class MaxIntPriority(Priority['MaxIntPriority']):
    def __init__(self, x: int):
        self.__x = x

    def compare_to(self, other: 'MaxIntPriority') -> int:
        return self.__x - other.__x

    def more(self) -> 'MaxIntPriority':
        return MaxIntPriority(self.__x + 1)

    def __eq__(self, other):
        if isinstance(other, MaxIntPriority):
            return self.__x == other.__x
        else:
            return False

    def __str__(self):
        return str(self.__x)


class PrioritizedItem(Generic[P, V]):
    def __init__(self, priority: P, value: V):
        self.__priority = priority
        self.__value = value

    def priority(self) -> P:
        return self.__priority

    def value(self) -> V:
        return self.__value

    def as_heap_node(self) -> HeapNode[P, V]:
        return HeapNode(self.__priority, self.__value)

    def __eq__(self, other):
        if isinstance(other, PrioritizedItem):
            return self.__priority == other.__priority and self.__value == other.__value
        else:
            return False

    def __str__(self):
        return f"[{self.__priority}, {self.__value}]"

    @staticmethod
    def prioritized_item(heap_node: HeapNode[P, V]):
        return PrioritizedItem(heap_node.key(), heap_node.value())


class PriorityQueue(AbstractQueue[PrioritizedItem[P, V]]):
    def __init__(self):
        self.__heap = BinaryHeap[P, V]([])

    def enqueue(self, item: PrioritizedItem[P, V]) -> None:
        self.__heap.push(item.as_heap_node())

    def dequeue(self) -> Optional[PrioritizedItem[P, V]]:
        return PrioritizedItem.prioritized_item(self.__heap.pop())

    def peak(self) -> Optional[PrioritizedItem[P, V]]:
        return PrioritizedItem.prioritized_item(self.__heap.peak())

    def change_priority(self, i: int, priority: P):
        self.__heap.change_key(i, priority)

    def __delitem__(self, i: int):
        del self.__heap[i]

    def is_empty(self) -> bool:
        return self.__heap.is_empty()

    def as_list(self) -> List[PrioritizedItem[P, V]]:
        return list(map(PrioritizedItem.prioritized_item, self.__heap.as_list()))
