#!/usr/bin/python3
from sys import argv

count = len(argv)
if count ==  1:
    print("1 argument:")
else:
    print("{} arguments:".format(count-1))

for n in range(1, count):
    print("{}: {} ".format(n,argv[n]))
