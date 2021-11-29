from abc import ABC, abstractmethod, ABCMeta
from typing import TypeVar, Generic, List, Optional, Iterator

K = TypeVar('K', bound='Key')
V = TypeVar('V')
N = TypeVar('N', bound='HeapNode')


class Key(Generic[K], metaclass=ABCMeta):

    @abstractmethod
    def compare_to(self, other: K) -> int:
        pass

    @abstractmethod
    def more(self) -> K:
        pass


class MinIntKey(Key['MinIntKey']):
    def __init__(self, x: int):
        self.__x = x

    def compare_to(self, other: 'MinIntKey') -> int:
        return other.__x - self.__x

    def more(self) -> 'MinIntKey':
        return MinIntKey(self.__x - 1)

    def __eq__(self, other):
        if isinstance(other, MinIntKey):
            return self.__x == other.__x
        else:
            return False

    def __str__(self):
        return str(self.__x)


class MaxIntKey(Key['MaxIntKey']):
    def __init__(self, x: int):
        self.__x = x

    def compare_to(self, other: 'MaxIntKey') -> int:
        return self.__x - other.__x

    def more(self) -> 'MaxIntKey':
        return MaxIntKey(self.__x + 1)

    def __eq__(self, other):
        if isinstance(other, MaxIntKey):
            return self.__x == other.__x
        else:
            return False

    def __str__(self):
        return str(self.__x)


class HeapNode(ABC, Generic[K, V, N]):

    @abstractmethod
    def key(self) -> K:
        pass

    @abstractmethod
    def value(self) -> V:
        pass

    @abstractmethod
    def copy(self, key: K) -> N:
        pass


class Entry(HeapNode[K, V, 'Entry']):
    def __init__(self, key: K, value: V):
        self.__key = key
        self.__value = value

    def key(self) -> K:
        return self.__key

    def value(self) -> V:
        return self.__value

    def copy(self, key: K) -> N:
        return Entry(key, self.__value)

    def __eq__(self, other: 'Entry'):
        if isinstance(other, Entry):
            return self.__key == other.__key and self.__value == other.__value
        else:
            return False

    def __str__(self):
        return f"[{self.__key}, {self.__value}]"


class Unit(HeapNode[K, K, 'Unit']):
    def __init__(self, key: K):
        self.__key = key

    def key(self) -> K:
        return self.__key

    def value(self) -> K:
        return self.__key

    def copy(self, key: K) -> N:
        return Unit(self.__key)

    def __eq__(self, other: 'Unit'):
        if isinstance(other, Unit):
            return self.__key == other.__key
        else:
            return False

    def __str__(self):
        return str({self.__key})


class Heap(Generic[K, V], ABC):
    def __init__(self, number_of_children, data: List[HeapNode[K, V, N]]):
        if number_of_children < 2:
            raise ValueError("Number of children must be greater than 1")
        self.__number_of_children = number_of_children
        self.__data: List[HeapNode[K, V, N]] = data
        for i in range(len(data) // self.__number_of_children - 1, -1, -1):
            self.__sift_down(i)

    def push(self, item: HeapNode[K, V, N]) -> None:
        self.__data.append(item)
        self.__sift_up(0, len(self.__data) - 1)

    def pop(self) -> Optional[HeapNode[K, V, N]]:
        return self.__pop()

    def peak(self) -> Optional[HeapNode[K, V, N]]:
        return self.__data[0] if self.__data else None

    def change_key(self, i: int, key: K) -> None:
        if i < len(self.__data):
            item_key = self.__data[i].key()
            self.__data[i] = self.__data[i].copy(key)
            if self.__data[i].key().compare_to(item_key) > 0:
                self.__sift_up(0, i)
            else:
                self.__sift_down(i)
        else:
            raise IndexError("index out of range")

    def __delitem__(self, i: int):
        if i < len(self.__data):
            root = self.__data[0]
            self.__data[i] = root.copy(root.key().more())
            self.__sift_up(0, i)
            self.__pop()
        else:
            raise IndexError("index out of range")

    def as_list(self) -> List[HeapNode[K, V, N]]:
        return self.__data[:]

    def is_empty(self) -> bool:
        return not self.__data

    def __pop(self) -> Optional[HeapNode[K, V, N]]:
        last = self.__data.pop()
        if self.__data:
            result = self.__data[0]
            self.__data[0] = last
            self.__sift_down(0)
            return result
        return last

    def __sift_up(self, start_i: int, i: int) -> None:
        item = self.__data[i]
        while i > start_i:
            parent_i = self.__parent_i(i)
            parent = self.__data[parent_i]
            if item.key().compare_to(parent.key()) > 0:
                self.__data[i] = parent
                i = parent_i
                continue
            break
        self.__data[i] = item

    def __sift_down(self, i: int) -> None:
        size = len(self.__data)
        start_i = i
        item = self.__data[i]
        child_i = self.__first_child_i(i)
        while child_i < size:
            for right_i in self.__right_children_i(i):
                if not (self.__data[child_i].key().compare_to(self.__data[right_i].key()) > 0):
                    child_i = right_i
            self.__data[i] = self.__data[child_i]
            i = child_i
            child_i = self.__first_child_i(i)
        self.__data[i] = item
        self.__sift_up(start_i, i)

    def __first_child_i(self, parent_i: int) -> int:
        return self.__number_of_children * parent_i + 1

    def __right_children_i(self, parent_i: int) -> Iterator[int]:
        for i in range(1, self.__number_of_children):
            child_i = self.__number_of_children * parent_i + i + 1
            if child_i < len(self.__data):
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
        self.__sift_up(0, len(self.__data) - 1)

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
                self.__sift_up(0, i)
            else:
                self.__sift_down(i)
        else:
            raise IndexError("index out of range")

    def as_list(self):
        return self.__data[:]

    def is_empty(self):
        return not self.__data

    def __sift_up(self, start_i, i):
        item = self.__data[i]
        while i > start_i:
            parent_i = self.__parent_i(i)
            parent = self.__data[parent_i]
            if item < parent:
                self.__data[i] = parent
                i = parent_i
                continue
            break
        self.__data[i] = item

    def __sift_down(self, i):
        size = len(self.__data)
        start_i = i
        item = self.__data[i]
        child_i = self.__first_child_i(i)
        while child_i < size:
            right_i = child_i + 1
            if right_i < size and self.__data[child_i] >= self.__data[right_i]:
                child_i = right_i
            self.__data[i] = self.__data[child_i]
            i = child_i
            child_i = self.__first_child_i(i)
        self.__data[i] = item
        self.__sift_up(start_i, i)

    @staticmethod
    def __first_child_i(parent_i):
        return 2 * parent_i + 1

    @staticmethod
    def __parent_i(child_i):
        return (child_i - 1) >> 1
