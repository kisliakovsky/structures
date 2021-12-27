# pylint: skip-file
"""This module contains implementation of 'AVL tree' data structure"""

from typing import TypeVar, Generic, List, Optional, Iterator

from src.stack import Stack

Value = TypeVar('Value')


class AvlTree(Generic[Value]):
    def __init__(self):
        self.__size = 0
        self.__root: Optional[AvlTree.Node[Value]] = None

    class Node(Generic[Value]):
        def __init__(
                self,
                value: Value,
                parent: Optional['AvlTree.Node[Value]'],
                left_child: Optional['AvlTree.Node[Value]'],
                right_child: Optional['AvlTree.Node[Value]'],
                height: int
        ):
            self.__value: Value = value
            self.__parent: Optional['AvlTree.Node[Value]'] = parent
            self.__left_child: Optional['AvlTree.Node[Value]'] = left_child
            self.__right_child: Optional['AvlTree.Node[Value]'] = right_child
            self.__height: int = height

        def __lt__(self, other: 'AvlTree.Node[Value]') -> bool:
            return self.__value < other.__value

        def __gt__(self, other: 'AvlTree.Node[Value]') -> bool:
            return self.__value > other.__value

        def balance_factor(self) -> int:
            return self.__left_height() - self.__right_height()

        def __left_height(self) -> int:
            return self.__left_child.__height + 1 if self.__has_left_child() else 0

        def __right_height(self) -> int:
            return self.__right_child.__height + 1 if self.__has_right_child() else 0

        def is_leaf(self):
            return self.__is_leaf()

        def __is_leaf(self):
            return not (self.__has_left_child() or self.__has_right_child())

        def has_left_child(self) -> bool:
            return self.__has_left_child()

        def __has_left_child(self) -> bool:
            return self.__left_child is not None

        def has_right_child(self) -> bool:
            return self.__has_right_child()

        def __has_right_child(self) -> bool:
            return self.__right_child is not None

        def has_parent(self) -> bool:
            return self.__has_parent()

        def __has_parent(self) -> bool:
            return self.__parent is not None

        def is_in_range(
                self,
                minimum: 'Optional[AvlTree.Node[Value]]',
                maximum: 'Optional[AvlTree.Node[Value]]'
        ) -> bool:
            minimum_condition = minimum is None or minimum.__value <= self.__value
            maximum_condition = maximum is None or self.__value < maximum.__value
            return minimum_condition and maximum_condition

        def bind_left_child(self, left_child: 'AvlTree.Node[Value]'):
            self.__left_child = left_child
            left_child.__parent = self

        def unbind_left_child(self):
            if self.has_left_child():
                self.__left_child.__parent = None
            self.__left_child = None

        def bind_right_child(self, right_child: 'AvlTree.Node[Value]'):
            self.__right_child = right_child
            right_child.__parent = self

        def unbind_right_child(self):
            if self.has_right_child():
                self.__right_child.__parent = None
            self.__right_child = None

        def recalculate_height(self) -> None:
            if self.__has_left_child():
                left_height = self.__left_height()
                if self.__has_right_child():
                    self.__height = max(left_height, self.__right_height())
                else:
                    self.__height = left_height
            else:
                if self.__has_right_child():
                    self.__height = self.__right_height()
                else:
                    self.__height = 0

        def swap_values(self, node: 'AvlTree.Node[Value]') -> None:
            self.__value, node.__value = node.__value, self.__value

        def left_child(self) -> 'AvlTree.Node[Value]':
            return self.__left_child

        def right_child(self) -> 'AvlTree.Node[Value]':
            return self.__right_child

        def parent(self) -> 'AvlTree.Node[Value]':
            return self.__parent

        def put_value(self, values: List[Value]) -> None:
            values.append(self.__value)

        def has_value(self, value: Value) -> bool:
            return self.__value == value

        def __str__(self) -> str:
            return f'Value {self.__value}, ' \
                   f'Left value {self.__left_child.__value if self.__left_child is not None else None}, ' \
                   f'Right value {self.__right_child.__value if self.__right_child is not None else None}, ' \
                   f'Parent value {self.__parent.__value if self.__parent is not None else None} ' \
                   f'Height {self.__height}'

        def __repr__(self) -> str:
            return str(self)

    def add(self, value: Value) -> None:
        new_node = AvlTree.Node(value, None, None, None, 0)
        if self.__size > 0:
            node = self.__root
            while not node.is_leaf():
                if node < new_node:
                    if node.has_right_child():
                        node = node.right_child()
                    else:
                        break
                else:
                    if node.has_left_child():
                        node = node.left_child()
                    else:
                        break
            if node < new_node:
                node.bind_right_child(new_node)
            else:
                node.bind_left_child(new_node)
            self.__recalculate_heights(node)
            if node.has_parent():
                parent = node.parent()
                balance_factor = parent.balance_factor()
                if balance_factor > 1:
                    if new_node < node:
                        self.__rotate_right(parent)
                    else:
                        self.__rotate_left_and_right(parent)
                elif balance_factor < -1:
                    if new_node > node:
                        self.__rotate_left(parent)
                    else:
                        self.__rotate_right_and_left(parent)
        else:
            self.__root = new_node
        self.__size += 1

    def __contains__(self, value: Value) -> bool:
        result = False
        for node in self.__walk_in_order(self.__root):
            if node.has_value(value):
                result = True
                break
        return result

    def delete(self, value: Value) -> None:
        node_to_delete = None
        for node in self.__walk_in_order(self.__root):
            if node.has_value(value):
                node_to_delete = node
                break
        if node_to_delete is not None:
            if node_to_delete.is_leaf():
                self.__skip_leaf(node_to_delete)
            elif node_to_delete.has_left_child() and node_to_delete.has_right_child():
                prev = node_to_delete.left_child()
                while prev.has_right_child():
                    prev = prev.right_child()
                node_to_delete.swap_values(prev)
                node_to_delete = prev
                if node_to_delete.has_left_child():
                    self.__skip_node(node_to_delete, node_to_delete.left_child())
                else:
                    self.__skip_leaf(node_to_delete)
            elif node_to_delete.has_left_child():
                self.__skip_node(node_to_delete, node_to_delete.left_child())
            elif node_to_delete.has_right_child():
                self.__skip_node(node_to_delete, node_to_delete.right_child())
            self.__size -= 1

    def __skip_leaf(self, leaf: Node[Value]) -> None:
        if leaf.has_parent():
            parent = leaf.parent()
            if parent.has_left_child() and parent.left_child() == leaf:
                parent.unbind_left_child()
            else:
                parent.unbind_right_child()
            self.__recalculate_heights(parent)
        else:
            self.__root = None

    def __skip_node(self, node: 'AvlTree.Node[Value]', child: 'AvlTree.Node[Value]') -> None:
        if node.has_parent():
            parent = node.parent()
            if parent.has_left_child() and parent.left_child() == node:
                parent.bind_left_child(child)
            else:
                parent.bind_right_child(child)
            self.__recalculate_heights(parent)
        else:
            self.__root = child

    def __rotate_left_and_right(self, z: 'AvlTree.Node[Value]') -> None:
        if z.has_left_child():
            x = z.left_child()
            self.__rotate_left(x)
            self.__rotate_right(z)

    def __rotate_right_and_left(self, z: 'AvlTree.Node[Value]') -> None:
        if z.has_right_child():
            x = z.right_child()
            self.__rotate_right(x)
            self.__rotate_left(z)

    def __rotate_left(self, x: 'AvlTree.Node[Value]') -> None:
        if x.has_right_child():
            y = x.right_child()
            if y.has_left_child():
                beta = y.left_child()
                x.bind_right_child(beta)
                self.__recalculate_heights(x)
            else:
                x.unbind_right_child()
                self.__recalculate_heights(x)
            if x.has_parent():
                p = x.parent()
                if p.has_left_child() and p.left_child() == x:
                    p.bind_left_child(y)
                else:
                    p.bind_right_child(y)
                self.__recalculate_heights(p)
            else:
                self.__root = y
            y.bind_left_child(x)
            self.__recalculate_heights(y)

    def __rotate_right(self, y: 'AvlTree.Node[Value]') -> None:
        if y.has_left_child():
            x = y.left_child()
            if x.has_right_child():
                beta = x.right_child()
                y.bind_left_child(beta)
                self.__recalculate_heights(y)
            else:
                y.unbind_left_child()
                self.__recalculate_heights(y)
            if y.has_parent():
                p = y.parent()
                if p.has_left_child() and p.left_child() == y:
                    p.bind_left_child(x)
                else:
                    p.bind_right_child(x)
                self.__recalculate_heights(p)
            else:
                self.__root = x
            x.bind_right_child(y)
            self.__recalculate_heights(x)

    @staticmethod
    def __recalculate_heights(node: Node[Value]) -> None:
        while node.has_parent():
            node.recalculate_height()
            node = node.parent()
        node.recalculate_height()

    def walk_in_order(self) -> List[Value]:
        values = []
        if self.__size > 0:
            for node in AvlTree.__walk_in_order(self.__root):
                node.put_value(values)
        return values

    @staticmethod
    def __walk_in_order(root: 'AvlTree.Node[Value]') -> Iterator['AvlTree.Node[Value]']:
        nodes = Stack[AvlTree.Node[Value]]()
        while not (nodes.is_empty() and root is None):
            while root is not None:
                nodes.push(root)
                root = root.left_child() if root.has_left_child() else None
            node = nodes.pop()
            root = node.right_child() if node.has_right_child() else None
            yield node
