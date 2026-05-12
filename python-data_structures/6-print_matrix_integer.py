#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element % int(len(row)) == 0:
                print("{:d}".format(element),end="\n")
            else:
                print("{:d}".format(element),end=" ")
