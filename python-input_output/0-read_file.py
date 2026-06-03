#!/usr/bin/python3
"""
module for
printing whats in
a file
"""


def read_file(filename=""):
    """
    prints file
    contents
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
