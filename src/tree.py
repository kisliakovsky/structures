from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

from src.stack import Stack

T = TypeVar('T')


class TreeHeight(ABC):

    @abstractmethod
    def height(self) -> int:
        pass


class TreeNode(TreeHeight, Generic[T]):
    def __init__(self, data: T):
        self.__data: T = data
        self.__parent: Optional[TreeNode[T]] = None
        self.__children: List[TreeNode[T]] = []

    def is_root(self) -> bool:
        return self.__parent is None

    def is_leaf(self) -> bool:
        return not self.__children

    def set_parent(self, parent) -> None:
        self.__parent = parent
        parent.__children.append(self)

    def height(self) -> int:
        return max(map(lambda node: node.height() + 1, self.__children)) if self.__children else 1


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
        else:
            height = self.__heights[child]
            if height != 0:
                return height
            else:
                new_height = 1 + self.__calculate_height(parent, self.__parents[parent])
                self.__heights[child] = new_height
                return new_height


class ChildrenTree(TreeHeight):
    def __init__(self, root: int, children_by_parents: List[List[int]]):
        if len(children_by_parents[root]) == 0:
            raise ValueError("Root must have children")
        self.__root = root
        self.__children_by_parents: List[List[int]] = children_by_parents
        self.__heights: List[int] = [0 for _ in children_by_parents]

    def height(self) -> int:
        self.__heights[self.__root] = 1
        stack = Stack[int]()
        stack.push(self.__root)
        while len(stack) != 0:
            parent = stack.pop()
            for child in self.__children_by_parents[parent]:
                self.__heights[child] = self.__heights[parent] + 1
                stack.push(child)
        return max(self.__heights)

    @staticmethod
    def children_tree(parents: List[int]):
        children_by_parents = [[] for _ in parents]
        root = None
        for child, parent in enumerate(parents):
            if parent != -1:
                children_by_parents[parent].append(child)
            else:
                root = child
        if root is not None:
            return ChildrenTree(root, children_by_parents)
        else:
            raise ValueError("Root must be specified")
