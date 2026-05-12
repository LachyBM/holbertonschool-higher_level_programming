#!/usr/bin/python3

def max_integer(my_list=[]):
    largest = 0 
    if not my_list:
        return None
    for n in range(0,len(my_list)):
        if my_list[n] > int(largest):
            largest = my_list[n]
    return largest

