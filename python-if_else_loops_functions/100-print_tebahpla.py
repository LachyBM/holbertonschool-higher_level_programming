#!/usr/bin/python3

for n in reversed(range(97, 123)):
    if n % 2 == 0:
        print("{}".format(chr(n)), end="")
    else:
        print("{}".format(chr(n-32)), end="")
