#!/usr/bin/python3
"""
module for geometry
of a recet
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    rectangle geo class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
