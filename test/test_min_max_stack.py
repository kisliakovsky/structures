from unittest import TestCase

from src.stack import MinMaxStack


class TestMinMaxStack(TestCase):

    def test_push(self):
        stack = MinMaxStack[int]()
        stack.push((None, None))
        stack.push((1, None))
        stack.push((None, 4))
        stack.push((2, None))
        stack.push((None, 3))
        self.assertEqual([(None, None), (1, None), (1, 4), (2, 4), (2, 3)], stack.as_list())

    def test_pop_and_push(self):
        stack = MinMaxStack[int]()
        stack.pop_and_push((None, None))
        stack.pop_and_push((1, None))
        stack.pop_and_push((None, 4))
        stack.pop_and_push((2, None))
        stack.pop_and_push((None, 3))
        self.assertEqual([(2, 3)], stack.as_list())

    def test_pop(self):
        stack = MinMaxStack[int]()
        stack.push((None, None))
        stack.push((1, None))
        stack.push((None, 4))
        stack.push((2, None))
        stack.push((None, 3))
        self.assertEqual((2, 3), stack.pop())
        self.assertEqual((2, 4), stack.pop())
        self.assertEqual((1, 4), stack.pop())
        self.assertEqual((1, None), stack.pop())
        self.assertEqual((None, None), stack.pop())
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        stack = MinMaxStack[int]()
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push((2, 3))
        self.assertEqual((2, 3), stack.peek())

    def test_is_empty(self):
        stack = MinMaxStack[int]()
        self.assertTrue(stack.is_empty())
        stack.push((2, 3))
        self.assertFalse(stack.is_empty())

    def test_size(self):
        stack = MinMaxStack[int]()
        self.assertEqual(0, len(stack))
        stack.push((None, None))
        self.assertEqual(1, len(stack))
        stack.push((1, None))
        self.assertEqual(2, len(stack))
        stack.push((None, 4))
        self.assertEqual(3, len(stack))
        stack.push((2, None))
        self.assertEqual(4, len(stack))
