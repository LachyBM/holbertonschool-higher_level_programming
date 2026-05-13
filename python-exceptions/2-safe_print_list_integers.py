#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        for n in range(0, x):
            if int(my_list[n]):
                print("{:d}".format(my_list[n]), end="")
            else:
                print("LOOP")
    except Exception:
        if x > n:
            print()
            return n
    print()
    return x
