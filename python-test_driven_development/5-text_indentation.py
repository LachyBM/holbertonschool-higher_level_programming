#!/usr/bin/python3
"""
module for printing text and new lines
"""


def text_indentation(text):
    """
    whenever the users text has certain symbols
    it will finish the line with them,
    and start up again after a newline betweeete
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    clean = False
    for char in text:
        if char not in '.?:,' and not (clean and char == ' '):
            print("{}".format(char), end="")
            clean = False
        else:
            if char in '.?:,':
                print("{}".format(char), end="\n\n")
                clean = True
