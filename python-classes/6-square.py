#!/usr/bin/python3
"""
module for a square
"""


class Square:
    """
    empty sqaure
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    def area(self):
        side = self.__size
        return (side*side)

    def my_print(self):
        size = self.__size
        position = self.__position

        if size == 0:
            print()

        for n in range(position[1]):
            print()

        for n in range(size):
            for n in range(position[0]):
                print("_", end="")
            for n in range(size):
                print("#", end="")
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = ()
        if self.__position[0] < 0 and self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        salf.__position = value
