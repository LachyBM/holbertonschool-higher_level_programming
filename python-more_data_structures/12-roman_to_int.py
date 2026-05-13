#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman = {"M": 1000,
             "D": 500,
             "C": 100,
             "L": 50,
             "X": 10,
             "V": 5,
             "I": 1}
    rev_roman = reversed(roman_string)
    count = 0
    prev = 0
    for char in rev_roman:
        current = roman.get(char)
        if current < prev:
            count -= current
        else:
            count += current
        prev = current
    return count
