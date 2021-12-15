from unittest import TestCase

from src.heap import Heap, MaxIntKey, Entry


class TestBinaryMaxHeap(TestCase):

    def test_init(self):
        heap = Heap[MaxIntKey, str](2, [
            Entry(MaxIntKey(14), 'A'),
            Entry(MaxIntKey(5), 'B'),
            Entry(MaxIntKey(7), 'C'),
            Entry(MaxIntKey(18), 'D'),
            Entry(MaxIntKey(42), 'E'),
            Entry(MaxIntKey(12), 'F'),
            Entry(MaxIntKey(11), 'G'),
            Entry(MaxIntKey(18), 'H'),
            Entry(MaxIntKey(29), 'I')
        ])
        self.assertEqual([
            Entry(MaxIntKey(42), 'E'),
            Entry(MaxIntKey(29), 'I'),
            Entry(MaxIntKey(12), 'F'),
            Entry(MaxIntKey(18), 'H'),
            Entry(MaxIntKey(5), 'B'),
            Entry(MaxIntKey(7), 'C'),
            Entry(MaxIntKey(11), 'G'),
            Entry(MaxIntKey(14), 'A'),
            Entry(MaxIntKey(18), 'D')
        ], heap.as_list())

    def test_push(self):
        heap = Heap[MaxIntKey, str](2, [])
        heap.push(Entry(MaxIntKey(14), 'A'))
        heap.push(Entry(MaxIntKey(5), 'B'))
        heap.push(Entry(MaxIntKey(7), 'C'))
        heap.push(Entry(MaxIntKey(18), 'D'))
        heap.push(Entry(MaxIntKey(42), 'E'))
        heap.push(Entry(MaxIntKey(12), 'F'))
        heap.push(Entry(MaxIntKey(11), 'G'))
        heap.push(Entry(MaxIntKey(18), 'H'))
        heap.push(Entry(MaxIntKey(29), 'I'))
        self.assertEqual([
            Entry(MaxIntKey(42), 'E'),
            Entry(MaxIntKey(29), 'I'),
            Entry(MaxIntKey(12), 'F'),
            Entry(MaxIntKey(18), 'D'),
            Entry(MaxIntKey(14), 'A'),
            Entry(MaxIntKey(7), 'C'),
            Entry(MaxIntKey(11), 'G'),
            Entry(MaxIntKey(5), 'B'),
            Entry(MaxIntKey(18), 'H')
        ], heap.as_list())

    def test_pop(self):
        heap = Heap[MaxIntKey, str](2, [])
        heap.push(Entry(MaxIntKey(14), 'A'))
        heap.push(Entry(MaxIntKey(5), 'B'))
        heap.push(Entry(MaxIntKey(7), 'C'))
        heap.push(Entry(MaxIntKey(18), 'D'))
        heap.push(Entry(MaxIntKey(42), 'E'))
        heap.push(Entry(MaxIntKey(12), 'F'))
        heap.push(Entry(MaxIntKey(11), 'G'))
        heap.push(Entry(MaxIntKey(18), 'H'))
        heap.push(Entry(MaxIntKey(29), 'I'))
        self.assertEqual(Entry(MaxIntKey(42), 'E'), heap.pop())
        self.assertEqual(Entry(MaxIntKey(29), 'I'), heap.pop())
        self.assertEqual(Entry(MaxIntKey(18), 'H'), heap.pop())
        self.assertEqual(Entry(MaxIntKey(18), 'D'), heap.pop())
        self.assertEqual(Entry(MaxIntKey(14), 'A'), heap.pop())
        self.assertEqual(Entry(MaxIntKey(12), 'F'), heap.pop())
        self.assertEqual(Entry(MaxIntKey(11), 'G'), heap.pop())
        self.assertEqual(Entry(MaxIntKey(7), 'C'), heap.pop())
        self.assertEqual(Entry(MaxIntKey(5), 'B'), heap.pop())

    def test_peek(self):
        heap = Heap[MaxIntKey, str](2, [])
        heap.push(Entry(MaxIntKey(14), 'A'))
        heap.push(Entry(MaxIntKey(5), 'B'))
        heap.push(Entry(MaxIntKey(7), 'C'))
        heap.push(Entry(MaxIntKey(18), 'D'))
        heap.push(Entry(MaxIntKey(42), 'E'))
        heap.push(Entry(MaxIntKey(12), 'F'))
        heap.push(Entry(MaxIntKey(11), 'G'))
        heap.push(Entry(MaxIntKey(18), 'H'))
        heap.push(Entry(MaxIntKey(29), 'I'))
        self.assertEqual(Entry(MaxIntKey(42), 'E'), heap.peek())
        self.assertEqual([
            Entry(MaxIntKey(42), 'E'),
            Entry(MaxIntKey(29), 'I'),
            Entry(MaxIntKey(12), 'F'),
            Entry(MaxIntKey(18), 'D'),
            Entry(MaxIntKey(14), 'A'),
            Entry(MaxIntKey(7), 'C'),
            Entry(MaxIntKey(11), 'G'),
            Entry(MaxIntKey(5), 'B'),
            Entry(MaxIntKey(18), 'H')
        ], heap.as_list())

    def test_change_key(self):
        heap = Heap[MaxIntKey, str](2, [])
        heap.push(Entry(MaxIntKey(14), 'A'))
        heap.push(Entry(MaxIntKey(5), 'B'))
        heap.push(Entry(MaxIntKey(7), 'C'))
        heap.push(Entry(MaxIntKey(18), 'D'))
        heap.push(Entry(MaxIntKey(42), 'E'))
        heap.push(Entry(MaxIntKey(12), 'F'))
        heap.push(Entry(MaxIntKey(11), 'G'))
        heap.push(Entry(MaxIntKey(18), 'H'))
        heap.push(Entry(MaxIntKey(29), 'I'))
        with self.assertRaises(IndexError):
            heap.change_key(9, MaxIntKey(20))
        heap.change_key(8, MaxIntKey(43))
        self.assertEqual(Entry(MaxIntKey(43), 'H'), heap.peek())

    def test_delete(self):
        heap = Heap[MaxIntKey, str](2, [])
        heap.push(Entry(MaxIntKey(14), 'A'))
        heap.push(Entry(MaxIntKey(5), 'B'))
        heap.push(Entry(MaxIntKey(7), 'C'))
        heap.push(Entry(MaxIntKey(18), 'D'))
        heap.push(Entry(MaxIntKey(42), 'E'))
        heap.push(Entry(MaxIntKey(12), 'F'))
        heap.push(Entry(MaxIntKey(11), 'G'))
        heap.push(Entry(MaxIntKey(18), 'H'))
        heap.push(Entry(MaxIntKey(29), 'I'))
        del heap[8]
        self.assertEqual([
            Entry(MaxIntKey(42), 'E'),
            Entry(MaxIntKey(29), 'I'),
            Entry(MaxIntKey(12), 'F'),
            Entry(MaxIntKey(18), 'D'),
            Entry(MaxIntKey(14), 'A'),
            Entry(MaxIntKey(7), 'C'),
            Entry(MaxIntKey(11), 'G'),
            Entry(MaxIntKey(5), 'B')
        ], heap.as_list())

    def test_is_empty(self):
        heap = Heap[MaxIntKey, str](2, [])
        self.assertTrue(heap.is_empty())
        heap.push(Entry(MaxIntKey(14), 'A'))
        self.assertFalse(heap.is_empty())
