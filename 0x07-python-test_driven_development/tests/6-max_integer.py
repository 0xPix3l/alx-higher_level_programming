"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittests """

    def test_ordered_list(self):
        """ Test ordered list. """
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """ Test unordered list. """
        unordered = [2, 3, 5, 1]
        self.assertEqual(max_integer(unordered), 5)

    def test_empty_list(self):
        """ Test empty list """
        empty = []
        self.assertEqual(max_integer(empty), None)
