#!/usr/bin/python3
"""
module for
converting
csv to json
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    convertion of csv
    to json
    """

    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open('data.json', 'w') as f:
            json.dump(data, f)

        return True
    except FileNotFoundError:
        return False
