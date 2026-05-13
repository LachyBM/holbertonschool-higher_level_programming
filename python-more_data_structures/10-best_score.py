#!/usr/bin/python3

def best_score(a_dictionary):
    if bool(a_dictionary) is False:
        return None
    result = max(a_dictionary, key=a_dictionary.get)
    return result
