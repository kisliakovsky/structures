"""This module contains implementations of 'tree' data structure"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional, Tuple, Iterator

from src.stack import Stack, MinMaxStack

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


class BinaryTree(Generic[Value]):
    def __init__(self, children_by_parents: List[Tuple[Value, int, int]]):
        self.__nodes: List[BinaryTree.Node[Value]] = []
        for i, entry in enumerate(children_by_parents):
            value, left_i, right_i = entry
            self.__nodes.append(BinaryTree.Node(i, value, left_i, right_i, self.__nodes))

    class Node(Generic[Value]):
        def __init__(
                self,
                index: int,
                value: Value,
                left_index: int,
                right_index: int,
                nodes: List['BinaryTree.Node[Value]']
        ):
            self.__index = index
            self.__value = value
            self.__left_index = left_index
            self.__right_index = right_index
            self.__nodes = nodes

        def has_left_child(self) -> bool:
            return self.__left_index != -1

        def has_right_child(self) -> bool:
            return self.__right_index != -1

        def __lt__(self, other: 'BinaryTree.Node[Value]') -> bool:
            return self.__value < other.__value

        def __gt__(self, other: 'BinaryTree.Node[Value]') -> bool:
            return self.__value > other.__value

        def is_in_range(
                self,
                minimum: 'Optional[BinaryTree.Node[Value]]',
                maximum: 'Optional[BinaryTree.Node[Value]]'
        ) -> bool:
            minumum_condition = minimum is None or minimum.__value <= self.__value
            maximum_condition = maximum is None or self.__value < maximum.__value
            return minumum_condition and maximum_condition

        def left_child(self) -> 'Optional[BinaryTree.Node[Value]]':
            if self.__left_index == -1:
                raise IndexError('Left child does not exist')
            return self.__nodes[self.__left_index]

        def right_child(self) -> 'Optional[BinaryTree.Node[Value]]':
            if self.__right_index == -1:
                raise IndexError('Right child does not exist')
            return self.__nodes[self.__right_index]

        def put_value(self, values: List[Value]) -> None:
            values.append(self.__value)

        def __str__(self) -> str:
            return str(f'Index {self.__index}, Value {self.__value}')

        def __repr__(self) -> str:
            return str(f'Index {self.__index}, Value {self.__value}')

    def is_search_tree(self) -> bool:
        result = True
        if self.__nodes:
            nodes = Stack[BinaryTree.Node[Value]]()
            root = self.__nodes[0]
            min_and_max = MinMaxStack[BinaryTree.Node[Value]]()
            while not (nodes.is_empty() and root is None):
                while root is not None:
                    nodes.push(root)
                    if root.has_left_child():
                        min_and_max.push((None, root))
                        root = root.left_child()
                    else:
                        root = None
                root = nodes.pop()
                min_node, max_node = min_and_max.peek() if not min_and_max.is_empty() else (None, None)
                if not root.is_in_range(min_node, max_node):
                    result = False
                    break
                if root.has_right_child():
                    min_and_max.pop_and_push((root, None))
                    root = root.right_child()
                else:
                    root = None
                    if not min_and_max.is_empty():
                        min_and_max.pop()
        return result

    def walk_in_order(self) -> List[int]:
        values = []
        for node in self.__walk_in_order(self.__nodes[0]):
            node.put_value(values)
        return values

    @staticmethod
    def __walk_in_order(root: 'BinaryTree.Node[Value]') -> Iterator['BinaryTree.Node[Value]']:
        nodes = Stack[BinaryTree.Node[Value]]()
        while not (nodes.is_empty() and root is None):
            while root is not None:
                nodes.push(root)
                root = root.left_child() if root.has_left_child() else None
            node = nodes.pop()
            root = node.right_child() if node.has_right_child() else None
            yield node

    def walk_pre_order(self) -> List[Value]:
        result = []
        if self.__nodes:
            self.__walk_pre_order(self.__nodes[0], result)
        return result

    def __walk_pre_order(self, root: 'BinaryTree.Node[Value]', result: List[int]) -> None:
        root.put_value(result)
        if root.has_left_child():
            self.__walk_pre_order(root.left_child(), result)
        if root.has_right_child():
            self.__walk_pre_order(root.right_child(), result)

    def walk_post_order(self) -> List[int]:
        result = []
        if self.__nodes:
            self.__walk_post_order(self.__nodes[0], result)
        return result

    def __walk_post_order(self, root: 'BinaryTree.Node[Value]', result: List[int]) -> None:
        if root.has_left_child():
            self.__walk_post_order(root.left_child(), result)
        if root.has_right_child():
            self.__walk_post_order(root.right_child(), result)
        root.put_value(result)
