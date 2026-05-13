#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for n in range(0, x):
            print("{}".format(my_list[n]), end="")
    except:
        if x > n:
            print()
            return n
    print()
    return x
