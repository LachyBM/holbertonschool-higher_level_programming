#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    largest = my_list[0]
    for n in range(0, len(my_list)):
        if my_list[n] > largest:
            largest = my_list[n]
    return largest
