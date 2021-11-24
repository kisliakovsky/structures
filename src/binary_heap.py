from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional, Tuple

T = TypeVar('T')


class HeapNode(Generic[T]):
    def __init__(self, key: int, value: T):
        self.__key = key
        self.__value = value

    def key(self) -> int:
        return self.__key

    def value(self) -> T:
        return self.__value

    def __eq__(self, other):
        if isinstance(other, HeapNode):
            return self.__key == other.__key and self.__value == other.__value
        else:
            return False

    def __str__(self):
        return f"[{self.__key}, {self.__value}]"

    @staticmethod
    def heap_node(key: int, node):
        return HeapNode(key, node.value())


class HeapNodeComparison(Generic[T], ABC):

    @abstractmethod
    def perform(self, first_node: HeapNode[T], second_node: HeapNode[T]) -> int:
        pass


class MinHeapNodeComparison(HeapNodeComparison[T]):

    def perform(self, first_node: HeapNode[T], second_node: HeapNode[T]) -> int:
        return second_node.key() - first_node.key()


class MaxHeapNodeComparison(HeapNodeComparison[T]):

    def perform(self, first_node: HeapNode[T], second_node: HeapNode[T]) -> int:
        return first_node.key() - second_node.key()


class BinaryHeap(Generic[T], ABC):
    def __init__(self, data: List[HeapNode[T]], comparison: HeapNodeComparison[T]):
        self.__comparison = comparison
        self.__swap_log: List[Tuple[int, int]] = []
        self.__data: List[HeapNode[T]] = data
        for i in range(len(data) // 2 - 1, -1, -1):
            self.__sift_down(i)

    def push(self, item: HeapNode[T]) -> None:
        self.__data.append(item)
        self.__sift_up(len(self.__data) - 1)

    def pop(self) -> Optional[HeapNode[T]]:
        return self.__pop()

    def peak(self) -> Optional[HeapNode[T]]:
        return self.__data[0] if self.__data else None

    def change_key(self, i: int, key: int) -> None:
        if i < len(self.__data):
            item = self.__data[i]
            self.__data[i] = HeapNode.heap_node(key, item)
            if self.__comparison.perform(self.__data[i], item) > 0:
                self.__sift_up(i)
            else:
                self.__sift_down(i)
        else:
            raise IndexError("index out of range")

    def __delitem__(self, i: int):
        if i < len(self.__data):
            if self.__comparison.perform(
                    HeapNode.heap_node(self.__data[0].key() - 1, self.__data[i]),
                    HeapNode.heap_node(self.__data[0].key() + 1, self.__data[i])
            ) > 0:
                new_node = HeapNode.heap_node(self.__data[0].key() - 1, self.__data[i])
            else:
                new_node = HeapNode.heap_node(self.__data[0].key() + 1, self.__data[i])
            self.__data[i] = new_node
            self.__sift_up(i)
            self.__pop()
        else:
            raise IndexError("index out of range")

    def as_list(self) -> List[HeapNode[T]]:
        return self.__data[:]

    def is_empty(self) -> bool:
        return not self.__data

    def swap_log(self) -> List[Tuple[int, int]]:
        return self.__swap_log[:]

    def __pop(self) -> Optional[HeapNode[T]]:
        if self.__data:
            result = self.__data[0]
            self.__swap(-1, 0)
            self.__data.pop()
            self.__sift_down(0)
            return result
        else:
            return None

    def __sift_up(self, i: int) -> None:
        while i > 0 and self.__should_be_lower_than(self.__parent_i(i), i):
            parent_i = self.__parent_i(i)
            self.__swap(parent_i, i)
            i = parent_i

    def __swap(self, i: int, j: int):
        self.__swap_log.append((i, j))
        self.__data[i], self.__data[j] = self.__data[j], self.__data[i]

    def __sift_down(self, i: int) -> None:
        extreme_i = None
        while extreme_i != i:
            extreme_i = i
            left_child_i = self.__left_child_i(i)
            if self.__should_be_higher_than(left_child_i, extreme_i):
                extreme_i = left_child_i
            right_child_i = self.__right_child_i(i)
            if self.__should_be_higher_than(right_child_i, extreme_i):
                extreme_i = right_child_i
            if i != extreme_i:
                self.__swap(i, extreme_i)
                i = extreme_i
                extreme_i = None

    def __should_be_higher_than(self, i: int, j: int) -> bool:
        return self.__comparison.perform(self.__data[i], self.__data[j]) > 0 if i < len(self.__data) else False

    def __should_be_lower_than(self, i: int, j: int) -> bool:
        return self.__comparison.perform(self.__data[i], self.__data[j]) < 0

    @staticmethod
    def __left_child_i(parent_i: int) -> Optional[int]:
        return 2 * parent_i + 1

    @staticmethod
    def __right_child_i(parent_i: int) -> Optional[int]:
        return 2 * parent_i + 2

    @staticmethod
    def __parent_i(child_i: int) -> int:
        return (child_i - 1) // 2


class BinaryMaxHeap(BinaryHeap[T]):
    def __init__(self, data: List[HeapNode[T]]):
        super().__init__(data, MaxHeapNodeComparison())


class BinaryMinHeap(BinaryHeap[T]):
    def __init__(self, data: List[HeapNode[T]]):
        super().__init__(data, MinHeapNodeComparison())
