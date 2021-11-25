from unittest import TestCase

from src.binary_heap import BinaryHeap, HeapNode, MaxIntKey


class TestBinaryMaxHeap(TestCase):

    def test_init(self):
        heap = BinaryHeap[MaxIntKey, str]([
            HeapNode(MaxIntKey(14), 'A'),
            HeapNode(MaxIntKey(5), 'B'),
            HeapNode(MaxIntKey(7), 'C'),
            HeapNode(MaxIntKey(18), 'D'),
            HeapNode(MaxIntKey(42), 'E'),
            HeapNode(MaxIntKey(12), 'F'),
            HeapNode(MaxIntKey(11), 'G'),
            HeapNode(MaxIntKey(18), 'H'),
            HeapNode(MaxIntKey(29), 'I')
        ])
        self.assertEqual([
            HeapNode(MaxIntKey(42), 'E'),
            HeapNode(MaxIntKey(29), 'I'),
            HeapNode(MaxIntKey(12), 'F'),
            HeapNode(MaxIntKey(18), 'H'),
            HeapNode(MaxIntKey(5), 'B'),
            HeapNode(MaxIntKey(7), 'C'),
            HeapNode(MaxIntKey(11), 'G'),
            HeapNode(MaxIntKey(14), 'A'),
            HeapNode(MaxIntKey(18), 'D')
        ], heap.as_list())

    def test_push(self):
        heap = BinaryHeap[MaxIntKey, str]([])
        heap.push(HeapNode(MaxIntKey(14), 'A'))
        heap.push(HeapNode(MaxIntKey(5), 'B'))
        heap.push(HeapNode(MaxIntKey(7), 'C'))
        heap.push(HeapNode(MaxIntKey(18), 'D'))
        heap.push(HeapNode(MaxIntKey(42), 'E'))
        heap.push(HeapNode(MaxIntKey(12), 'F'))
        heap.push(HeapNode(MaxIntKey(11), 'G'))
        heap.push(HeapNode(MaxIntKey(18), 'H'))
        heap.push(HeapNode(MaxIntKey(29), 'I'))
        self.assertEqual([
            HeapNode(MaxIntKey(42), 'E'),
            HeapNode(MaxIntKey(29), 'I'),
            HeapNode(MaxIntKey(12), 'F'),
            HeapNode(MaxIntKey(18), 'D'),
            HeapNode(MaxIntKey(14), 'A'),
            HeapNode(MaxIntKey(7), 'C'),
            HeapNode(MaxIntKey(11), 'G'),
            HeapNode(MaxIntKey(5), 'B'),
            HeapNode(MaxIntKey(18), 'H')
        ], heap.as_list())

    def test_pop(self):
        heap = BinaryHeap[MaxIntKey, str]([])
        heap.push(HeapNode(MaxIntKey(14), 'A'))
        heap.push(HeapNode(MaxIntKey(5), 'B'))
        heap.push(HeapNode(MaxIntKey(7), 'C'))
        heap.push(HeapNode(MaxIntKey(18), 'D'))
        heap.push(HeapNode(MaxIntKey(42), 'E'))
        heap.push(HeapNode(MaxIntKey(12), 'F'))
        heap.push(HeapNode(MaxIntKey(11), 'G'))
        heap.push(HeapNode(MaxIntKey(18), 'H'))
        heap.push(HeapNode(MaxIntKey(29), 'I'))
        self.assertEqual(HeapNode(MaxIntKey(42), 'E'), heap.pop())
        self.assertEqual(HeapNode(MaxIntKey(29), 'I'), heap.pop())
        self.assertEqual(HeapNode(MaxIntKey(18), 'H'), heap.pop())
        self.assertEqual(HeapNode(MaxIntKey(18), 'D'), heap.pop())
        self.assertEqual(HeapNode(MaxIntKey(14), 'A'), heap.pop())
        self.assertEqual(HeapNode(MaxIntKey(12), 'F'), heap.pop())
        self.assertEqual(HeapNode(MaxIntKey(11), 'G'), heap.pop())
        self.assertEqual(HeapNode(MaxIntKey(7), 'C'), heap.pop())
        self.assertEqual(HeapNode(MaxIntKey(5), 'B'), heap.pop())

    def test_peak(self):
        heap = BinaryHeap[MaxIntKey, str]([])
        heap.push(HeapNode(MaxIntKey(14), 'A'))
        heap.push(HeapNode(MaxIntKey(5), 'B'))
        heap.push(HeapNode(MaxIntKey(7), 'C'))
        heap.push(HeapNode(MaxIntKey(18), 'D'))
        heap.push(HeapNode(MaxIntKey(42), 'E'))
        heap.push(HeapNode(MaxIntKey(12), 'F'))
        heap.push(HeapNode(MaxIntKey(11), 'G'))
        heap.push(HeapNode(MaxIntKey(18), 'H'))
        heap.push(HeapNode(MaxIntKey(29), 'I'))
        self.assertEqual(HeapNode(MaxIntKey(42), 'E'), heap.peak())
        self.assertEqual([
            HeapNode(MaxIntKey(42), 'E'),
            HeapNode(MaxIntKey(29), 'I'),
            HeapNode(MaxIntKey(12), 'F'),
            HeapNode(MaxIntKey(18), 'D'),
            HeapNode(MaxIntKey(14), 'A'),
            HeapNode(MaxIntKey(7), 'C'),
            HeapNode(MaxIntKey(11), 'G'),
            HeapNode(MaxIntKey(5), 'B'),
            HeapNode(MaxIntKey(18), 'H')
        ], heap.as_list())

    def test_change_key(self):
        heap = BinaryHeap[MaxIntKey, str]([])
        heap.push(HeapNode(MaxIntKey(14), 'A'))
        heap.push(HeapNode(MaxIntKey(5), 'B'))
        heap.push(HeapNode(MaxIntKey(7), 'C'))
        heap.push(HeapNode(MaxIntKey(18), 'D'))
        heap.push(HeapNode(MaxIntKey(42), 'E'))
        heap.push(HeapNode(MaxIntKey(12), 'F'))
        heap.push(HeapNode(MaxIntKey(11), 'G'))
        heap.push(HeapNode(MaxIntKey(18), 'H'))
        heap.push(HeapNode(MaxIntKey(29), 'I'))
        with self.assertRaises(IndexError):
            heap.change_key(9, MaxIntKey(20))
        heap.change_key(8, MaxIntKey(43))
        self.assertEqual(HeapNode(MaxIntKey(43), 'H'), heap.peak())

    def test_delete(self):
        heap = BinaryHeap[MaxIntKey, str]([])
        heap.push(HeapNode(MaxIntKey(14), 'A'))
        heap.push(HeapNode(MaxIntKey(5), 'B'))
        heap.push(HeapNode(MaxIntKey(7), 'C'))
        heap.push(HeapNode(MaxIntKey(18), 'D'))
        heap.push(HeapNode(MaxIntKey(42), 'E'))
        heap.push(HeapNode(MaxIntKey(12), 'F'))
        heap.push(HeapNode(MaxIntKey(11), 'G'))
        heap.push(HeapNode(MaxIntKey(18), 'H'))
        heap.push(HeapNode(MaxIntKey(29), 'I'))
        del heap[8]
        self.assertEqual([
            HeapNode(MaxIntKey(42), 'E'),
            HeapNode(MaxIntKey(29), 'I'),
            HeapNode(MaxIntKey(12), 'F'),
            HeapNode(MaxIntKey(18), 'D'),
            HeapNode(MaxIntKey(14), 'A'),
            HeapNode(MaxIntKey(7), 'C'),
            HeapNode(MaxIntKey(11), 'G'),
            HeapNode(MaxIntKey(5), 'B')
        ], heap.as_list())

    def test_is_empty(self):
        heap = BinaryHeap[MaxIntKey, str]([])
        self.assertTrue(heap.is_empty())
        heap.push(HeapNode(MaxIntKey(14), 'A'))
        self.assertFalse(heap.is_empty())
