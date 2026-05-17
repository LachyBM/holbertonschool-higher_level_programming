#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(max_integer([1, 2, 10, 3]), 10)

    def test_order(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_start(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single(self):
        self.assertEqual(max_integer([1]), 1)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -4, -10, -2]), -1)
    
    def test_one_negative(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_empty(self):
        self.assertEqual(max_integer([]))

if __name__ == "__main__":
    unittest.main()
