#!/usr/bin/python3

def multiple_returns(sentence):
    first = ""
    for char in sentence:
        if char in range(0) == "":
            first = "None"
        else:
            first = sentence[0]
    return len(sentence), first
