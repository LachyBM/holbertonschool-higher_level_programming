#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    counted = []
    for n in range(0,len(my_list)):
        if my_list[n] in counted:
            continue
        else:
            result += my_list[n]
            counted.append(my_list[n])
    return result
