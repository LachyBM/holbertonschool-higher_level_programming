#!/usr/bin/python3

from sys import argv

count = len(argv)

if __name__ == "__main__":
    final = 0
    for n in range (1, count):
        final += int(argv[n])

    print("{}".format(final))

