from unittest import TestCase

from src.binary_heap import HeapNode, BinaryMinHeap


class TestBinaryMinHeap(TestCase):

    def test_init(self):
        heap = BinaryMinHeap[str]([
            HeapNode[str]('A', 14),
            HeapNode[str]('B', 5),
            HeapNode[str]('C', 7),
            HeapNode[str]('D', 18),
            HeapNode[str]('E', 42),
            HeapNode[str]('F', 12),
            HeapNode[str]('G', 11),
            HeapNode[str]('H', 18),
            HeapNode[str]('I', 29)
        ])
        self.assertEqual([
            HeapNode[str]('B', 5),
            HeapNode[str]('A', 14),
            HeapNode[str]('C', 7),
            HeapNode[str]('D', 18),
            HeapNode[str]('E', 42),
            HeapNode[str]('F', 12),
            HeapNode[str]('G', 11),
            HeapNode[str]('H', 18),
            HeapNode[str]('I', 29)
        ], heap.as_list())

    def test_swap_log(self):
        heap = BinaryMinHeap[int]([
            HeapNode[int](7, 7),
            HeapNode[int](6, 6),
            HeapNode[int](5, 5),
            HeapNode[int](4, 4),
            HeapNode[int](3, 3),
            HeapNode[int](2, 2)
        ])
        self.assertEqual([
            (2, 5),
            (1, 4),
            (0, 2),
            (2, 5)
        ], heap.swap_log())

    def test_push(self):
        heap = BinaryMinHeap[str]([])
        heap.push(HeapNode[str]('A', 14))
        heap.push(HeapNode[str]('B', 5))
        heap.push(HeapNode[str]('C', 7))
        heap.push(HeapNode[str]('D', 18))
        heap.push(HeapNode[str]('E', 42))
        heap.push(HeapNode[str]('F', 12))
        heap.push(HeapNode[str]('G', 11))
        heap.push(HeapNode[str]('H', 18))
        heap.push(HeapNode[str]('I', 29))
        self.assertEqual([
            HeapNode[str]('B', 5),
            HeapNode[str]('A', 14),
            HeapNode[str]('C', 7),
            HeapNode[str]('D', 18),
            HeapNode[str]('E', 42),
            HeapNode[str]('F', 12),
            HeapNode[str]('G', 11),
            HeapNode[str]('H', 18),
            HeapNode[str]('I', 29)
        ], heap.as_list())

    def test_pop(self):
        heap = BinaryMinHeap[str]([])
        heap.push(HeapNode[str]('A', 14))
        heap.push(HeapNode[str]('B', 5))
        heap.push(HeapNode[str]('C', 7))
        heap.push(HeapNode[str]('D', 18))
        heap.push(HeapNode[str]('E', 42))
        heap.push(HeapNode[str]('F', 12))
        heap.push(HeapNode[str]('G', 11))
        heap.push(HeapNode[str]('H', 18))
        heap.push(HeapNode[str]('I', 29))
        self.assertEqual(HeapNode[str]('B', 5), heap.pop())
        self.assertEqual(HeapNode[str]('C', 7), heap.pop())
        self.assertEqual(HeapNode[str]('G', 11), heap.pop())
        self.assertEqual(HeapNode[str]('F', 12), heap.pop())
        self.assertEqual(HeapNode[str]('A', 14), heap.pop())
        self.assertEqual(HeapNode[str]('D', 18), heap.pop())
        self.assertEqual(HeapNode[str]('H', 18), heap.pop())
        self.assertEqual(HeapNode[str]('I', 29), heap.pop())
        self.assertEqual(HeapNode[str]('E', 42), heap.pop())

    def test_peak(self):
        heap = BinaryMinHeap[str]([])
        heap.push(HeapNode[str]('A', 14))
        heap.push(HeapNode[str]('B', 5))
        heap.push(HeapNode[str]('C', 7))
        heap.push(HeapNode[str]('D', 18))
        heap.push(HeapNode[str]('E', 42))
        heap.push(HeapNode[str]('F', 12))
        heap.push(HeapNode[str]('G', 11))
        heap.push(HeapNode[str]('H', 18))
        heap.push(HeapNode[str]('I', 29))
        self.assertEqual(HeapNode[str]('B', 5), heap.peak())
        self.assertEqual([
            HeapNode[str]('B', 5),
            HeapNode[str]('A', 14),
            HeapNode[str]('C', 7),
            HeapNode[str]('D', 18),
            HeapNode[str]('E', 42),
            HeapNode[str]('F', 12),
            HeapNode[str]('G', 11),
            HeapNode[str]('H', 18),
            HeapNode[str]('I', 29)
        ], heap.as_list())

    def test_change_priority(self):
        heap = BinaryMinHeap[str]([])
        heap.push(HeapNode[str]('A', 14))
        heap.push(HeapNode[str]('B', 5))
        heap.push(HeapNode[str]('C', 7))
        heap.push(HeapNode[str]('D', 18))
        heap.push(HeapNode[str]('E', 42))
        heap.push(HeapNode[str]('F', 12))
        heap.push(HeapNode[str]('G', 11))
        heap.push(HeapNode[str]('H', 18))
        heap.push(HeapNode[str]('I', 29))
        with self.assertRaises(IndexError):
            heap.change_priority(9, 20)
        heap.change_priority(8, 4)
        self.assertEqual(HeapNode[str]('I', 4), heap.peak())

    def test_delete(self):
        heap = BinaryMinHeap[str]([])
        heap.push(HeapNode[str]('A', 14))
        heap.push(HeapNode[str]('B', 5))
        heap.push(HeapNode[str]('C', 7))
        heap.push(HeapNode[str]('D', 18))
        heap.push(HeapNode[str]('E', 42))
        heap.push(HeapNode[str]('F', 12))
        heap.push(HeapNode[str]('G', 11))
        heap.push(HeapNode[str]('H', 18))
        heap.push(HeapNode[str]('I', 29))
        del heap[8]
        self.assertEqual([
            HeapNode[str]('B', 5),
            HeapNode[str]('A', 14),
            HeapNode[str]('C', 7),
            HeapNode[str]('D', 18),
            HeapNode[str]('E', 42),
            HeapNode[str]('F', 12),
            HeapNode[str]('G', 11),
            HeapNode[str]('H', 18)
        ], heap.as_list())

    def test_is_empty(self):
        heap = BinaryMinHeap[str]([])
        self.assertTrue(heap.is_empty())
        heap.push(HeapNode[str]('A', 14))
        self.assertFalse(heap.is_empty())
