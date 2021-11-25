from unittest import TestCase

from src.binary_heap import HeapNode, BinaryHeap, MinIntKey


class TestBinaryMinHeap(TestCase):

    def test_init(self):
        heap = BinaryHeap[MinIntKey, str]([
            HeapNode[MinIntKey, str](MinIntKey(14), 'A'),
            HeapNode[MinIntKey, str](MinIntKey(5), 'B'),
            HeapNode[MinIntKey, str](MinIntKey(7), 'C'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'D'),
            HeapNode[MinIntKey, str](MinIntKey(42), 'E'),
            HeapNode[MinIntKey, str](MinIntKey(12), 'F'),
            HeapNode[MinIntKey, str](MinIntKey(11), 'G'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'H'),
            HeapNode[MinIntKey, str](MinIntKey(29), 'I')
        ])
        self.assertEqual([
            HeapNode[MinIntKey, str](MinIntKey(5), 'B'),
            HeapNode[MinIntKey, str](MinIntKey(14), 'A'),
            HeapNode[MinIntKey, str](MinIntKey(7), 'C'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'D'),
            HeapNode[MinIntKey, str](MinIntKey(42), 'E'),
            HeapNode[MinIntKey, str](MinIntKey(12), 'F'),
            HeapNode[MinIntKey, str](MinIntKey(11), 'G'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'H'),
            HeapNode[MinIntKey, str](MinIntKey(29), 'I')
        ], heap.as_list())

    def test_swap_log(self):
        heap = BinaryHeap[MinIntKey, str]([
            HeapNode[MinIntKey, int](MinIntKey(7), 7),
            HeapNode[MinIntKey, int](MinIntKey(6), 6),
            HeapNode[MinIntKey, int](MinIntKey(5), 5),
            HeapNode[MinIntKey, int](MinIntKey(4), 4),
            HeapNode[MinIntKey, int](MinIntKey(3), 3),
            HeapNode[MinIntKey, int](MinIntKey(2), 2)
        ])
        self.assertEqual([
            (2, 5),
            (1, 4),
            (0, 2),
            (2, 5)
        ], heap.swap_log())

    def test_push(self):
        heap = BinaryHeap[MinIntKey, str]([])
        heap.push(HeapNode[MinIntKey, str](MinIntKey(14), 'A'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(5), 'B'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(7), 'C'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'D'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(42), 'E'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(12), 'F'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(11), 'G'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'H'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(29), 'I'))
        self.assertEqual([
            HeapNode[MinIntKey, str](MinIntKey(5), 'B'),
            HeapNode[MinIntKey, str](MinIntKey(14), 'A'),
            HeapNode[MinIntKey, str](MinIntKey(7), 'C'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'D'),
            HeapNode[MinIntKey, str](MinIntKey(42), 'E'),
            HeapNode[MinIntKey, str](MinIntKey(12), 'F'),
            HeapNode[MinIntKey, str](MinIntKey(11), 'G'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'H'),
            HeapNode[MinIntKey, str](MinIntKey(29), 'I')
        ], heap.as_list())

    def test_pop(self):
        heap = BinaryHeap[MinIntKey, str]([])
        heap.push(HeapNode[MinIntKey, str](MinIntKey(14), 'A'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(5), 'B'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(7), 'C'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'D'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(42), 'E'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(12), 'F'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(11), 'G'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'H'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(29), 'I'))
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(5), 'B'), heap.pop())
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(7), 'C'), heap.pop())
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(11), 'G'), heap.pop())
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(12), 'F'), heap.pop())
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(14), 'A'), heap.pop())
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(18), 'D'), heap.pop())
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(18), 'H'), heap.pop())
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(29), 'I'), heap.pop())
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(42), 'E'), heap.pop())

    def test_peak(self):
        heap = BinaryHeap[MinIntKey, str]([])
        heap.push(HeapNode[MinIntKey, str](MinIntKey(14), 'A'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(5), 'B'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(7), 'C'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'D'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(42), 'E'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(12), 'F'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(11), 'G'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'H'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(29), 'I'))
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(5), 'B'), heap.peak())
        self.assertEqual([
            HeapNode[MinIntKey, str](MinIntKey(5), 'B'),
            HeapNode[MinIntKey, str](MinIntKey(14), 'A'),
            HeapNode[MinIntKey, str](MinIntKey(7), 'C'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'D'),
            HeapNode[MinIntKey, str](MinIntKey(42), 'E'),
            HeapNode[MinIntKey, str](MinIntKey(12), 'F'),
            HeapNode[MinIntKey, str](MinIntKey(11), 'G'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'H'),
            HeapNode[MinIntKey, str](MinIntKey(29), 'I')
        ], heap.as_list())

    def test_change_key(self):
        heap = BinaryHeap[MinIntKey, str]([])
        heap.push(HeapNode[MinIntKey, str](MinIntKey(14), 'A'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(5), 'B'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(7), 'C'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'D'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(42), 'E'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(12), 'F'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(11), 'G'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'H'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(29), 'I'))
        with self.assertRaises(IndexError):
            heap.change_key(9, MinIntKey(20))
        heap.change_key(8, MinIntKey(4))
        self.assertEqual(HeapNode[MinIntKey, str](MinIntKey(4), 'I'), heap.peak())

    def test_delete(self):
        heap = BinaryHeap[MinIntKey, str]([])
        heap.push(HeapNode[MinIntKey, str](MinIntKey(14), 'A'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(5), 'B'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(7), 'C'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'D'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(42), 'E'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(12), 'F'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(11), 'G'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(18), 'H'))
        heap.push(HeapNode[MinIntKey, str](MinIntKey(29), 'I'))
        del heap[8]
        self.assertEqual([
            HeapNode[MinIntKey, str](MinIntKey(5), 'B'),
            HeapNode[MinIntKey, str](MinIntKey(14), 'A'),
            HeapNode[MinIntKey, str](MinIntKey(7), 'C'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'D'),
            HeapNode[MinIntKey, str](MinIntKey(42), 'E'),
            HeapNode[MinIntKey, str](MinIntKey(12), 'F'),
            HeapNode[MinIntKey, str](MinIntKey(11), 'G'),
            HeapNode[MinIntKey, str](MinIntKey(18), 'H')
        ], heap.as_list())

    def test_is_empty(self):
        heap = BinaryHeap[MinIntKey, str]([])
        self.assertTrue(heap.is_empty())
        heap.push(HeapNode[MinIntKey, str](MinIntKey(14), 'A'))
        self.assertFalse(heap.is_empty())
