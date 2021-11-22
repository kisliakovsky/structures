from unittest import TestCase

from src.tree import ChildrenTree


class TestTreeNode(TestCase):

    def test_height(self):
        tree = ChildrenTree(1, [[], [3, 4], [], [], [0, 2]])
        self.assertEqual(3, tree.height())
