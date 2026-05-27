#!/usr/bin/python3
"""
Module to check if inherits
"""


def inherits_form(obj, a_class):
    """
    return true if instance but isnt that type
    else false
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
