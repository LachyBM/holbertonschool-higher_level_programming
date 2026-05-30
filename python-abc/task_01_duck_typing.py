#!/usr/bin/python3
"""
module for animal
noises
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    class for shapes
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    class for
    circle
    """

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius * self.__radius)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    class for rect
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (2 * self.__width) + (2 * self.__height)


def shape_info(Shape):
    """
    def for shape info
    """
    print("Area: {}".format(Shape.area()))
    print("Perimeter: {}".format(Shape.perimeter()))
