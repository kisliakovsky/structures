from unittest import TestCase

from src.tree import BinaryTreeNode


class TestBinaryTreeNode(TestCase):

    def test_has_left_child(self):
        nodes = []
        root = BinaryTreeNode(0, 1, 1, -1, nodes)
        nodes.append(root)
        left_child = BinaryTreeNode(1, 2, -1, -1, nodes)
        nodes.append(left_child)
        self.assertTrue(root.has_left_child())
        self.assertFalse(left_child.has_left_child())

    def test_has_right_child(self):
        nodes = []
        root = BinaryTreeNode(0, 1, -1, 1, nodes)
        nodes.append(root)
        right_child = BinaryTreeNode(1, 2, -1, -1, nodes)
        nodes.append(right_child)
        self.assertTrue(root.has_right_child())
        self.assertFalse(right_child.has_right_child())

    def test_is_in_range(self):
        nodes = []
        root = BinaryTreeNode(0, 1, -1, 1, nodes)
        self.assertTrue(root.is_in_range(None, None))
        nodes.append(root)
        right_child = BinaryTreeNode(1, 1, 2, 3, nodes)
        nodes.append(right_child)
        right_child_of_right_child = BinaryTreeNode(3, 2, -1, -1, nodes)
        nodes.append(right_child_of_right_child)
        self.assertTrue(right_child.is_in_range(root, right_child_of_right_child))
        left_child_of_right_child = BinaryTreeNode(2, 1, -1, -1, nodes)
        nodes.append(left_child_of_right_child)
        self.assertFalse(left_child_of_right_child.is_in_range(root, right_child))

    def test_left_child(self):
        nodes = []
        root = BinaryTreeNode(0, 1, 1, -1, nodes)
        nodes.append(root)
        left_child = BinaryTreeNode(1, 2, -1, -1, nodes)
        nodes.append(left_child)
        self.assertEqual(left_child, root.left_child())
        with self.assertRaises(IndexError):
            left_child.left_child()

    def test_right_child(self):
        nodes = []
        root = BinaryTreeNode(0, 1, -1, 1, nodes)
        nodes.append(root)
        right_child = BinaryTreeNode(1, 1, 2, 3, nodes)
        nodes.append(right_child)
        self.assertEqual(right_child, root.right_child())
        with self.assertRaises(IndexError):
            right_child.right_child()

    def test_put_value(self):
        nodes = []
        node = BinaryTreeNode(0, 1, 1, -1, nodes)
        nodes.append(node)
        values = []
        node.put_value(values)
        self.assertEqual([1], values)
