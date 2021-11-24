from unittest import TestCase

from src.binary_heap import BinaryMaxHeap, HeapNode


class TestBinaryMaxHeap(TestCase):

    def test_init(self):
        heap = BinaryMaxHeap[str]([
            HeapNode[str](14, 'A'),
            HeapNode[str](5, 'B'),
            HeapNode[str](7, 'C'),
            HeapNode[str](18, 'D'),
            HeapNode[str](42, 'E'),
            HeapNode[str](12, 'F'),
            HeapNode[str](11, 'G'),
            HeapNode[str](18, 'H'),
            HeapNode[str](29, 'I')
        ])
        self.assertEqual([
            HeapNode[str](42, 'E'),
            HeapNode[str](29, 'I'),
            HeapNode[str](12, 'F'),
            HeapNode[str](18, 'H'),
            HeapNode[str](5, 'B'),
            HeapNode[str](7, 'C'),
            HeapNode[str](11, 'G'),
            HeapNode[str](14, 'A'),
            HeapNode[str](18, 'D')
        ], heap.as_list())

    def test_push(self):
        heap = BinaryMaxHeap[str]([])
        heap.push(HeapNode[str](14, 'A'))
        heap.push(HeapNode[str](5, 'B'))
        heap.push(HeapNode[str](7, 'C'))
        heap.push(HeapNode[str](18, 'D'))
        heap.push(HeapNode[str](42, 'E'))
        heap.push(HeapNode[str](12, 'F'))
        heap.push(HeapNode[str](11, 'G'))
        heap.push(HeapNode[str](18, 'H'))
        heap.push(HeapNode[str](29, 'I'))
        self.assertEqual([
            HeapNode[str](42, 'E'),
            HeapNode[str](29, 'I'),
            HeapNode[str](12, 'F'),
            HeapNode[str](18, 'D'),
            HeapNode[str](14, 'A'),
            HeapNode[str](7, 'C'),
            HeapNode[str](11, 'G'),
            HeapNode[str](5, 'B'),
            HeapNode[str](18, 'H')
        ], heap.as_list())

    def test_pop(self):
        heap = BinaryMaxHeap[str]([])
        heap.push(HeapNode[str](14, 'A'))
        heap.push(HeapNode[str](5, 'B'))
        heap.push(HeapNode[str](7, 'C'))
        heap.push(HeapNode[str](18, 'D'))
        heap.push(HeapNode[str](42, 'E'))
        heap.push(HeapNode[str](12, 'F'))
        heap.push(HeapNode[str](11, 'G'))
        heap.push(HeapNode[str](18, 'H'))
        heap.push(HeapNode[str](29, 'I'))
        self.assertEqual(HeapNode[str](42, 'E'), heap.pop())
        self.assertEqual(HeapNode[str](29, 'I'), heap.pop())
        self.assertEqual(HeapNode[str](18, 'H'), heap.pop())
        self.assertEqual(HeapNode[str](18, 'D'), heap.pop())
        self.assertEqual(HeapNode[str](14, 'A'), heap.pop())
        self.assertEqual(HeapNode[str](12, 'F'), heap.pop())
        self.assertEqual(HeapNode[str](11, 'G'), heap.pop())
        self.assertEqual(HeapNode[str](7, 'C'), heap.pop())
        self.assertEqual(HeapNode[str](5, 'B'), heap.pop())

    def test_peak(self):
        heap = BinaryMaxHeap[str]([])
        heap.push(HeapNode[str](14, 'A'))
        heap.push(HeapNode[str](5, 'B'))
        heap.push(HeapNode[str](7, 'C'))
        heap.push(HeapNode[str](18, 'D'))
        heap.push(HeapNode[str](42, 'E'))
        heap.push(HeapNode[str](12, 'F'))
        heap.push(HeapNode[str](11, 'G'))
        heap.push(HeapNode[str](18, 'H'))
        heap.push(HeapNode[str](29, 'I'))
        self.assertEqual(HeapNode[str](42, 'E'), heap.peak())
        self.assertEqual([
            HeapNode[str](42, 'E'),
            HeapNode[str](29, 'I'),
            HeapNode[str](12, 'F'),
            HeapNode[str](18, 'D'),
            HeapNode[str](14, 'A'),
            HeapNode[str](7, 'C'),
            HeapNode[str](11, 'G'),
            HeapNode[str](5, 'B'),
            HeapNode[str](18, 'H')
        ], heap.as_list())

    def test_change_key(self):
        heap = BinaryMaxHeap[str]([])
        heap.push(HeapNode[str](14, 'A'))
        heap.push(HeapNode[str](5, 'B'))
        heap.push(HeapNode[str](7, 'C'))
        heap.push(HeapNode[str](18, 'D'))
        heap.push(HeapNode[str](42, 'E'))
        heap.push(HeapNode[str](12, 'F'))
        heap.push(HeapNode[str](11, 'G'))
        heap.push(HeapNode[str](18, 'H'))
        heap.push(HeapNode[str](29, 'I'))
        with self.assertRaises(IndexError):
            heap.change_key(9, 20)
        heap.change_key(8, 43)
        self.assertEqual(HeapNode[str](43, 'H'), heap.peak())

    def test_delete(self):
        heap = BinaryMaxHeap[str]([])
        heap.push(HeapNode[str](14, 'A'))
        heap.push(HeapNode[str](5, 'B'))
        heap.push(HeapNode[str](7, 'C'))
        heap.push(HeapNode[str](18, 'D'))
        heap.push(HeapNode[str](42, 'E'))
        heap.push(HeapNode[str](12, 'F'))
        heap.push(HeapNode[str](11, 'G'))
        heap.push(HeapNode[str](18, 'H'))
        heap.push(HeapNode[str](29, 'I'))
        del heap[8]
        self.assertEqual([
            HeapNode[str](42, 'E'),
            HeapNode[str](29, 'I'),
            HeapNode[str](12, 'F'),
            HeapNode[str](18, 'D'),
            HeapNode[str](14, 'A'),
            HeapNode[str](7, 'C'),
            HeapNode[str](11, 'G'),
            HeapNode[str](5, 'B')
        ], heap.as_list())

    def test_is_empty(self):
        heap = BinaryMaxHeap[str]([])
        self.assertTrue(heap.is_empty())
        heap.push(HeapNode[str](14, 'A'))
        self.assertFalse(heap.is_empty())
