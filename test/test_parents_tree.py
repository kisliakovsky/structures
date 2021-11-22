from unittest import TestCase

from src.tree import TreeNode, ParentsTree


class TestTreeNode(TestCase):

    def test_height(self):
        tree = ParentsTree([4, -1, 4, 1, 1])
        self.assertEqual(3, tree.height())
