#!/usr/bin/python3
"""
module to print
json file
"""
import json


def load_from_json_file(filename):
    """
    prints string
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
