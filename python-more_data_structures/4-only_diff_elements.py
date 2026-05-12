#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    common = []
    for n in set_1:
        if n not in set_2:
            common.append(n)
    for n in set_2:
        if n not in set_1:
            common.append(n)
    return common
