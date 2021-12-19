from unittest import TestCase

from src.tree import BinaryChildrenTree


class TestBinaryChildrenTree(TestCase):

    def test_walk_in_order(self):
        tree = BinaryChildrenTree([
            (4, 1, 2),
            (2, 3, 4),
            (5, -1, -1),
            (1, -1, -1),
            (3, -1, -1),
        ])
        self.assertEqual([1, 2, 3, 4, 5], tree.walk_in_order())

    def test_walk_pre_order(self):
        tree = BinaryChildrenTree([
            (4, 1, 2),
            (2, 3, 4),
            (5, -1, -1),
            (1, -1, -1),
            (3, -1, -1),
        ])
        self.assertEqual([4, 2, 1, 3, 5], tree.walk_pre_order())

    def test_walk_post_order(self):
        tree = BinaryChildrenTree([
            (4, 1, 2),
            (2, 3, 4),
            (5, -1, -1),
            (1, -1, -1),
            (3, -1, -1),
        ])
        self.assertEqual([1, 3, 2, 5, 4], tree.walk_post_order())
