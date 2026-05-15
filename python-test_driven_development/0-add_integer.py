#!/usr/bin/python3
"""
module for adding two integers
"""


def add_integer(a, b=98):
    """
    add the two integers together
    and print return the result
    if a or b not int, raise typeerror
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
