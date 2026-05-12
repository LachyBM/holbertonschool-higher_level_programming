#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list
    for n in range(0, len(my_list)):
        if my_list[n] % 2 == 0:
            new_list[n] = True
        else:
            new_list[n] = False
    return new_list
