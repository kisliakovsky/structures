from unittest import TestCase

from src.heap import Heap, MinIntKey, Entry


class TestBinaryMinHeap(TestCase):

    def test_init(self):
        heap = Heap[MinIntKey, str](3, [
            Entry(MinIntKey(14), 'A'),
            Entry(MinIntKey(5), 'B'),
            Entry(MinIntKey(7), 'C'),
            Entry(MinIntKey(18), 'D'),
            Entry(MinIntKey(42), 'E'),
            Entry(MinIntKey(12), 'F'),
            Entry(MinIntKey(11), 'G'),
            Entry(MinIntKey(18), 'H'),
            Entry(MinIntKey(29), 'I')
        ])
        self.assertEqual([
            Entry(MinIntKey(5), 'B'),
            Entry(MinIntKey(11), 'G'),
            Entry(MinIntKey(7), 'C'),
            Entry(MinIntKey(18), 'D'),
            Entry(MinIntKey(42), 'E'),
            Entry(MinIntKey(12), 'F'),
            Entry(MinIntKey(14), 'A'),
            Entry(MinIntKey(18), 'H'),
            Entry(MinIntKey(29), 'I')
        ], heap.as_list())

    def test_push(self):
        heap = Heap[MinIntKey, str](3, [])
        heap.push(Entry(MinIntKey(14), 'A'))
        heap.push(Entry(MinIntKey(5), 'B'))
        heap.push(Entry(MinIntKey(7), 'C'))
        heap.push(Entry(MinIntKey(18), 'D'))
        heap.push(Entry(MinIntKey(42), 'E'))
        heap.push(Entry(MinIntKey(12), 'F'))
        heap.push(Entry(MinIntKey(11), 'G'))
        heap.push(Entry(MinIntKey(18), 'H'))
        heap.push(Entry(MinIntKey(29), 'I'))
        self.assertEqual([
            Entry(MinIntKey(5), 'B'),
            Entry(MinIntKey(11), 'G'),
            Entry(MinIntKey(7), 'C'),
            Entry(MinIntKey(18), 'D'),
            Entry(MinIntKey(42), 'E'),
            Entry(MinIntKey(14), 'A'),
            Entry(MinIntKey(12), 'F'),
            Entry(MinIntKey(18), 'H'),
            Entry(MinIntKey(29), 'I')
        ], heap.as_list())

    def test_pop(self):
        heap = Heap[MinIntKey, str](3, [])
        heap.push(Entry(MinIntKey(14), 'A'))
        heap.push(Entry(MinIntKey(5), 'B'))
        heap.push(Entry(MinIntKey(7), 'C'))
        heap.push(Entry(MinIntKey(18), 'D'))
        heap.push(Entry(MinIntKey(42), 'E'))
        heap.push(Entry(MinIntKey(12), 'F'))
        heap.push(Entry(MinIntKey(11), 'G'))
        heap.push(Entry(MinIntKey(18), 'H'))
        heap.push(Entry(MinIntKey(29), 'I'))
        self.assertEqual(Entry(MinIntKey(5), 'B'), heap.pop())
        self.assertEqual(Entry(MinIntKey(7), 'C'), heap.pop())
        self.assertEqual(Entry(MinIntKey(11), 'G'), heap.pop())
        self.assertEqual(Entry(MinIntKey(12), 'F'), heap.pop())
        self.assertEqual(Entry(MinIntKey(14), 'A'), heap.pop())
        self.assertEqual(Entry(MinIntKey(18), 'H'), heap.pop())
        self.assertEqual(Entry(MinIntKey(18), 'D'), heap.pop())
        self.assertEqual(Entry(MinIntKey(29), 'I'), heap.pop())
        self.assertEqual(Entry(MinIntKey(42), 'E'), heap.pop())

    def test_peek(self):
        heap = Heap[MinIntKey, str](3, [])
        heap.push(Entry(MinIntKey(14), 'A'))
        heap.push(Entry(MinIntKey(5), 'B'))
        heap.push(Entry(MinIntKey(7), 'C'))
        heap.push(Entry(MinIntKey(18), 'D'))
        heap.push(Entry(MinIntKey(42), 'E'))
        heap.push(Entry(MinIntKey(12), 'F'))
        heap.push(Entry(MinIntKey(11), 'G'))
        heap.push(Entry(MinIntKey(18), 'H'))
        heap.push(Entry(MinIntKey(29), 'I'))
        self.assertEqual(Entry(MinIntKey(5), 'B'), heap.peek())
        self.assertEqual([
            Entry(MinIntKey(5), 'B'),
            Entry(MinIntKey(11), 'G'),
            Entry(MinIntKey(7), 'C'),
            Entry(MinIntKey(18), 'D'),
            Entry(MinIntKey(42), 'E'),
            Entry(MinIntKey(14), 'A'),
            Entry(MinIntKey(12), 'F'),
            Entry(MinIntKey(18), 'H'),
            Entry(MinIntKey(29), 'I')
        ], heap.as_list())

    def test_change_key(self):
        heap = Heap[MinIntKey, str](3, [])
        heap.push(Entry(MinIntKey(14), 'A'))
        heap.push(Entry(MinIntKey(5), 'B'))
        heap.push(Entry(MinIntKey(7), 'C'))
        heap.push(Entry(MinIntKey(18), 'D'))
        heap.push(Entry(MinIntKey(42), 'E'))
        heap.push(Entry(MinIntKey(12), 'F'))
        heap.push(Entry(MinIntKey(11), 'G'))
        heap.push(Entry(MinIntKey(18), 'H'))
        heap.push(Entry(MinIntKey(29), 'I'))
        with self.assertRaises(IndexError):
            heap.change_key(9, MinIntKey(20))
        heap.change_key(8, MinIntKey(4))
        self.assertEqual(Entry(MinIntKey(4), 'I'), heap.peek())

    def test_delete(self):
        heap = Heap[MinIntKey, str](3, [])
        heap.push(Entry(MinIntKey(14), 'A'))
        heap.push(Entry(MinIntKey(5), 'B'))
        heap.push(Entry(MinIntKey(7), 'C'))
        heap.push(Entry(MinIntKey(18), 'D'))
        heap.push(Entry(MinIntKey(42), 'E'))
        heap.push(Entry(MinIntKey(12), 'F'))
        heap.push(Entry(MinIntKey(11), 'G'))
        heap.push(Entry(MinIntKey(18), 'H'))
        heap.push(Entry(MinIntKey(29), 'I'))
        del heap[8]
        self.assertEqual([
            Entry(MinIntKey(5), 'B'),
            Entry(MinIntKey(11), 'G'),
            Entry(MinIntKey(7), 'C'),
            Entry(MinIntKey(18), 'D'),
            Entry(MinIntKey(42), 'E'),
            Entry(MinIntKey(14), 'A'),
            Entry(MinIntKey(12), 'F'),
            Entry(MinIntKey(18), 'H')
        ], heap.as_list())

    def test_is_empty(self):
        heap = Heap[MinIntKey, str](3, [])
        self.assertTrue(heap.is_empty())
        heap.push(Entry(MinIntKey(14), 'A'))
        self.assertFalse(heap.is_empty())
