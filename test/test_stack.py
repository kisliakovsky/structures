from unittest import TestCase

from src.stack import Stack


class TestStack(TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('A')
        stack.push('B')
        stack.push('C')
        self.assertEqual(['A', 'B', 'C'], stack.as_list())

    def test_pop(self):
        stack = Stack()
        stack.push('A')
        self.assertEqual('A', stack.pop())
        self.assertEqual(None, stack.pop())
        self.assertEqual([], stack.as_list())
