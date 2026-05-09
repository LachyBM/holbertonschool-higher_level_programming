#!/usr/bin/python3

for n in range(0, 9):
    for x in range(n + 1, 10):
        if (n, x) == (8, 9):
            print("{0}{1}".format(n, x))
        else:
            print("{0}{1}".format(n, x), end=", ")
