from unittest import TestCase

from src.avl_tree import AvlTree


class TestAvlTree(TestCase):

    def test_add(self):
        tree = AvlTree[int]()
        tree.add(33)
        tree.add(13)
        tree.add(53)
        tree.add(11)
        tree.add(21)
        tree.add(61)
        tree.add(8)
        tree.add(9)
        self.assertEqual([8, 9, 11, 13, 21, 33, 53, 61], tree.walk_in_order())

    def test_contains(self):
        tree = AvlTree[int]()
        tree.add(33)
        tree.add(13)
        tree.add(53)
        tree.add(11)
        tree.add(21)
        tree.add(61)
        tree.add(8)
        tree.add(9)
        self.assertTrue(9 in tree)
        self.assertFalse(10 in tree)

    def test_delete(self):
        tree = AvlTree[int]()
        tree.add(33)
        tree.add(13)
        tree.add(53)
        tree.add(11)
        tree.add(21)
        tree.add(61)
        tree.add(8)
        tree.add(9)
        tree.delete(13)
        self.assertEqual([8, 9, 11, 21, 33, 53, 61], tree.walk_in_order())
