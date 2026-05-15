#!/usr/bin/python3
"""
module for printing a square 
with hashtags
"""


def print_square(size):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for n in range(size):
        for n in range(size):
            print("#", end="")
        print()   
