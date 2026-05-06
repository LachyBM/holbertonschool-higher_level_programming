#!/usr/bin/python3
from sys import argv

count = len(argv)
if __name__ == "__main__":
    if count == 2 :
        print("1 argument:")
    elif count == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(count - 1))

    for n in range(1, count):
        print("{}: {}".format(n, argv[n]))
