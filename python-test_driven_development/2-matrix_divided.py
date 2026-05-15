#!/usr/bin/python3
"""
module for dividing numbers in a matrix
"""


def matrix_divided(matrix, div):
    """
    divide all numbers in the matrix
    by the number entered
    em =  error message as without
    it breaks pycodestyle
    """

    em = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(em)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(em)
    if not all(isinstance(n, (int, float)) for row in matrix for n in row):
        raise TypeError(em)
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for n in row:
            if n is None:
                new_row.append(None)
            else:
                new_row.append(round(n / div, 2))
        new_matrix.append(new_row)
    return new_matrix
