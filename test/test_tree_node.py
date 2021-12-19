from unittest import TestCase

from src.tree import TreeNode


class TestTreeNode(TestCase):

    def test_is_root(self):
        root = TreeNode(3)
        child = TreeNode(9)
        child.set_parent(root)
        self.assertTrue(root.is_root())
        self.assertFalse(child.is_root())

    def test_is_leaf(self):
        root = TreeNode(3)
        child = TreeNode(9)
        child.set_parent(root)
        self.assertTrue(child.is_leaf())
        self.assertFalse(root.is_leaf())

    def test_height(self):
        one = TreeNode(1)
        two = TreeNode(1)
        three = TreeNode(1)
        four = TreeNode(1)
        five = TreeNode(1)
        six = TreeNode(1)
        seven = TreeNode(1)
        eight = TreeNode(1)
        nine = TreeNode(1)
        two.set_parent(seven)
        eight.set_parent(seven)
        seven.set_parent(one)
        five.set_parent(six)
        one.set_parent(six)
        four.set_parent(six)
        nine.set_parent(three)
        six.set_parent(three)
        self.assertEqual(1, two.height())
        self.assertEqual(1, eight.height())
        self.assertEqual(1, five.height())
        self.assertEqual(1, four.height())
        self.assertEqual(1, nine.height())
        self.assertEqual(2, seven.height())
        self.assertEqual(3, one.height())
        self.assertEqual(4, six.height())
        self.assertEqual(5, three.height())

    def test_value(self):
        node = TreeNode('A')
        self.assertEqual('A', node.value())
