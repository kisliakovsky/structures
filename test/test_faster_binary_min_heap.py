from unittest import TestCase

from src.heap import FasterMinHeap


class TestFasterBinaryMinHeap(TestCase):

    def test_init(self):
        heap = FasterMinHeap([14, 5, 7, 18, 42, 12, 11, 18, 29])
        self.assertEqual([5, 14, 7, 18, 42, 12, 11, 18, 29], heap.as_list())

    def test_push(self):
        heap = FasterMinHeap([])
        heap.push(14)
        heap.push(5)
        heap.push(7)
        heap.push(18)
        heap.push(42)
        heap.push(12)
        heap.push(11)
        heap.push(18)
        heap.push(29)
        self.assertEqual([5, 14, 7, 18, 42, 12, 11, 18, 29], heap.as_list())

    def test_pop(self):
        heap = FasterMinHeap([])
        heap.push(14)
        heap.push(5)
        heap.push(7)
        heap.push(18)
        heap.push(42)
        heap.push(12)
        heap.push(11)
        heap.push(18)
        heap.push(29)
        self.assertEqual(5, heap.pop())
        self.assertEqual(7, heap.pop())
        self.assertEqual(11, heap.pop())
        self.assertEqual(12, heap.pop())
        self.assertEqual(14, heap.pop())
        self.assertEqual(18, heap.pop())
        self.assertEqual(18, heap.pop())
        self.assertEqual(29, heap.pop())
        self.assertEqual(42, heap.pop())

    def test_peak(self):
        heap = FasterMinHeap([])
        heap.push(14)
        heap.push(5)
        heap.push(7)
        heap.push(18)
        heap.push(42)
        heap.push(12)
        heap.push(11)
        heap.push(18)
        heap.push(29)
        self.assertEqual(5, heap.peak())
        self.assertEqual([5, 14, 7, 18, 42, 12, 11, 18, 29], heap.as_list())

    def test_change_key(self):
        heap = FasterMinHeap([])
        heap.push(14)
        heap.push(5)
        heap.push(7)
        heap.push(18)
        heap.push(42)
        heap.push(12)
        heap.push(11)
        heap.push(18)
        heap.push(29)
        with self.assertRaises(IndexError):
            heap.change_key(9, 20)
        heap.change_key(8, 4)
        self.assertEqual(4, heap.peak())

    def test_is_empty(self):
        heap = FasterMinHeap([])
        self.assertTrue(heap.is_empty())
        heap.push(14)
        self.assertFalse(heap.is_empty())
