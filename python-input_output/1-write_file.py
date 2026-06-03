#!/usr/bin/python3
"""
module for
printing a file
i create
"""


def write_file(filename="", text=""):
    """
    write file
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
