#!/usr/bin/python3
"""
module for
printing a file
i create
"""


def append_write(filename="", text=""):
    """
    append a write
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
