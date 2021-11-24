from unittest import TestCase

from src.binary_heap import HeapNode, BinaryMinHeap


class TestBinaryMinHeap(TestCase):

    def test_init(self):
        heap = BinaryMinHeap[str]([
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
            HeapNode[str](5, 'B'),
            HeapNode[str](14, 'A'),
            HeapNode[str](7, 'C'),
            HeapNode[str](18, 'D'),
            HeapNode[str](42, 'E'),
            HeapNode[str](12, 'F'),
            HeapNode[str](11, 'G'),
            HeapNode[str](18, 'H'),
            HeapNode[str](29, 'I')
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
            HeapNode[str](5, 'B'),
            HeapNode[str](14, 'A'),
            HeapNode[str](7, 'C'),
            HeapNode[str](18, 'D'),
            HeapNode[str](42, 'E'),
            HeapNode[str](12, 'F'),
            HeapNode[str](11, 'G'),
            HeapNode[str](18, 'H'),
            HeapNode[str](29, 'I')
        ], heap.as_list())

    def test_pop(self):
        heap = BinaryMinHeap[str]([])
        heap.push(HeapNode[str](14, 'A'))
        heap.push(HeapNode[str](5, 'B'))
        heap.push(HeapNode[str](7, 'C'))
        heap.push(HeapNode[str](18, 'D'))
        heap.push(HeapNode[str](42, 'E'))
        heap.push(HeapNode[str](12, 'F'))
        heap.push(HeapNode[str](11, 'G'))
        heap.push(HeapNode[str](18, 'H'))
        heap.push(HeapNode[str](29, 'I'))
        self.assertEqual(HeapNode[str](5, 'B'), heap.pop())
        self.assertEqual(HeapNode[str](7, 'C'), heap.pop())
        self.assertEqual(HeapNode[str](11, 'G'), heap.pop())
        self.assertEqual(HeapNode[str](12, 'F'), heap.pop())
        self.assertEqual(HeapNode[str](14, 'A'), heap.pop())
        self.assertEqual(HeapNode[str](18, 'D'), heap.pop())
        self.assertEqual(HeapNode[str](18, 'H'), heap.pop())
        self.assertEqual(HeapNode[str](29, 'I'), heap.pop())
        self.assertEqual(HeapNode[str](42, 'E'), heap.pop())

    def test_peak(self):
        heap = BinaryMinHeap[str]([])
        heap.push(HeapNode[str](14, 'A'))
        heap.push(HeapNode[str](5, 'B'))
        heap.push(HeapNode[str](7, 'C'))
        heap.push(HeapNode[str](18, 'D'))
        heap.push(HeapNode[str](42, 'E'))
        heap.push(HeapNode[str](12, 'F'))
        heap.push(HeapNode[str](11, 'G'))
        heap.push(HeapNode[str](18, 'H'))
        heap.push(HeapNode[str](29, 'I'))
        self.assertEqual(HeapNode[str](5, 'B'), heap.peak())
        self.assertEqual([
            HeapNode[str](5, 'B'),
            HeapNode[str](14, 'A'),
            HeapNode[str](7, 'C'),
            HeapNode[str](18, 'D'),
            HeapNode[str](42, 'E'),
            HeapNode[str](12, 'F'),
            HeapNode[str](11, 'G'),
            HeapNode[str](18, 'H'),
            HeapNode[str](29, 'I')
        ], heap.as_list())

    def test_change_key(self):
        heap = BinaryMinHeap[str]([])
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
        heap.change_key(8, 4)
        self.assertEqual(HeapNode[str](4, 'I'), heap.peak())

    def test_delete(self):
        heap = BinaryMinHeap[str]([])
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
            HeapNode[str](5, 'B'),
            HeapNode[str](14, 'A'),
            HeapNode[str](7, 'C'),
            HeapNode[str](18, 'D'),
            HeapNode[str](42, 'E'),
            HeapNode[str](12, 'F'),
            HeapNode[str](11, 'G'),
            HeapNode[str](18, 'H')
        ], heap.as_list())

    def test_is_empty(self):
        heap = BinaryMinHeap[str]([])
        self.assertTrue(heap.is_empty())
        heap.push(HeapNode[str](14, 'A'))
        self.assertFalse(heap.is_empty())
