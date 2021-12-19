"""This module contains implementations of 'tree' data structure"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional, Tuple

from src.stack import Stack

Value = TypeVar('Value')


class TreeHeight(ABC):

    @abstractmethod
    def height(self) -> int:
        pass


class TreeNode(TreeHeight, Generic[Value]):
    def __init__(self, value: Value):
        self.__value: Value = value
        self.__parent: Optional[TreeNode[Value]] = None
        self.__children: List[TreeNode[Value]] = []

    def is_root(self) -> bool:
        return self.__parent is None

    def is_leaf(self) -> bool:
        return not self.__children

    def set_parent(self, parent: 'TreeNode[Value]') -> None:
        self.__parent = parent
        parent.__children.append(self)

    def height(self) -> int:
        return max(map(lambda node: node.height() + 1, self.__children)) if self.__children else 1

    def value(self) -> Value:
        return self.__value


class ParentsTree(TreeHeight):
    def __init__(self, parents: List[int]):
        self.__parents: List[int] = parents
        self.__heights: List[int] = [0 for _ in parents]

    def height(self) -> int:
        for child, parent in enumerate(self.__parents):
            self.__calculate_height(child, parent)
        return max(self.__heights)

    def __calculate_height(self, child, parent) -> int:
        if parent == -1:
            new_height = 1
            self.__heights[child] = new_height
            return new_height
        height = self.__heights[child]
        if height != 0:
            return height
        new_height = 1 + self.__calculate_height(parent, self.__parents[parent])
        self.__heights[child] = new_height
        return new_height


class ChildrenTree(TreeHeight):
    def __init__(self, root: int, children_by_parents: List[List[int]]):
        if len(children_by_parents[root]) == 0:
            raise ValueError('Root must have children')
        self.__root = root
        self.__children_by_parents: List[List[int]] = children_by_parents
        self.__heights: List[int] = [0 for _ in children_by_parents]

    def height(self) -> int:
        self.__heights[self.__root] = 1
        stack = Stack[int]()
        stack.push(self.__root)
        while not stack.is_empty():
            parent = stack.pop()
            for child in self.__children_by_parents[parent]:
                self.__heights[child] = self.__heights[parent] + 1
                stack.push(child)
        return max(self.__heights)

    @staticmethod
    def children_tree(parents: List[int]) -> 'ChildrenTree':
        children_by_parents = [[] for _ in parents]
        root = None
        for child, parent in enumerate(parents):
            if parent != -1:
                children_by_parents[parent].append(child)
            else:
                root = child
        if root is None:
            raise ValueError('Root must be specified')
        return ChildrenTree(root, children_by_parents)


class BinaryChildrenTree(Generic[Value]):
    def __init__(self, children_by_parents: List[Tuple[Value, int, int]]):
        self.__children_by_parents = children_by_parents

    def walk_in_order(self) -> List[int]:
        result = []
        if self.__children_by_parents:
            self.__walk_in_order(0, result)
        return result

    def __walk_in_order(self, i: int, result: List[int]):
        value, left_i, right_i = self.__children_by_parents[i]
        if left_i != -1:
            self.__walk_in_order(left_i, result)
        result.append(value)
        if right_i != -1:
            self.__walk_in_order(right_i, result)

    def walk_pre_order(self) -> List[int]:
        result = []
        if self.__children_by_parents:
            self.__walk_pre_order(0, result)
        return result

    def __walk_pre_order(self, i: int, result: List[int]):
        value, left_i, right_i = self.__children_by_parents[i]
        result.append(value)
        if left_i != -1:
            self.__walk_pre_order(left_i, result)
        if right_i != -1:
            self.__walk_pre_order(right_i, result)

    def walk_post_order(self) -> List[int]:
        result = []
        if self.__children_by_parents:
            self.__walk_post_order(0, result)
        return result

    def __walk_post_order(self, i: int, result: List[int]):
        value, left_i, right_i = self.__children_by_parents[i]
        if left_i != -1:
            self.__walk_post_order(left_i, result)
        if right_i != -1:
            self.__walk_post_order(right_i, result)
        result.append(value)
