#!/usr/bin/python3
"""
module for a dragon
"""


class SwimMixin:
    """
    swim mixin
    """

    def swim(self):
        print("The creatue swims!")


class FlyMixin:
    """
    fly mixin
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    dragon
    """

    def roar(self):
        print("The dragon roars!")
