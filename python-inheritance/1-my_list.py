#!/usr/bin/python3
"""
Module for printing sorted list
"""


class MyList(list):
    """
    get list of numbers (int)
    and print them sorted
    """

    def print_sorted(self):
        print(sorted(self))
