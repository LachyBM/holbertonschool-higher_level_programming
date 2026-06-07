#!/usr/bin/python3
"""
module for
pascals triangle
"""


def pascal_triangle(n):
    """
    create pascal triangle
    and if n <= 0 empty
    """

    if n <= 0:
        return []

    printer = []
    for x in range(n):
        row = [1] * (x + 1)
        for i in range(1, x):
            row[i] = printer[x-1][i-1] + printer[x-1][i]
        printer.append(row)

    return printer
