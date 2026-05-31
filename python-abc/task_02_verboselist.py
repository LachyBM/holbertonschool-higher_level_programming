#!/usr/bin/python3
"""
module for animal
noises
"""


class VerboseList(list):
    """
    class to edit
    a list
    """

    def append(self, vlist):
        super().append(vlist)
        print("Added [{}] to the list.".format(vlist))

    def extend(self, vlist):
        super().extend(vlist)
        print("Extended the list with [{}] items".format(len(vlist)))

    def remove(self, vlist):
        print("Removed [{}] from the list".format(vlist))
        super().remove(vlist)

    def pop(self, index=-1):
        vlist = self[index]
        print("Popped [{}] from the list".format(vlist))
        return super().pop(index)
