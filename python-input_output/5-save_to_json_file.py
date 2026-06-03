#!/usr/bin/python3
"""
module to print
json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    prints string
    """
    with open(filename, "a", encoding="utf-8") as f:
        json.dump(my_obj, f)
