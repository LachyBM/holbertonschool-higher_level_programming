#!/usr/bin/python3
"""
module for animal
noises
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    class for animal sounds
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    class for dog
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    class for cat
    """

    def sound(self):
        return "Meow"
