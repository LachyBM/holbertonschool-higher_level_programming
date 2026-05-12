#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    for n in range(0, len(my_list)):
        if n == idx:
            for n in range(n, len(my_list) + 1):
                if n >= len(my_list) - 1:
                    del my_list[-1]
                    return my_list
                else:
                    my_list[n] = my_list[n + 1]
    return my_list
