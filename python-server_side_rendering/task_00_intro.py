#!/usr/bin/python

import os

def generate_invitations(template_content, attendees):

    if type(template_content) is not str:
        print("Template is not a string")
        return
    if template_content == "":
        print( "Template is empty, no output files generated.")
        return
    if type(attendees) is not list:
        print("Attendees needs to be in a list")
        return
    if all(isinstance(people, dict) for people in attendees) is False:
        print("Attendees need to have a dictionary of there data")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated")
        return
    
    printer = ''
    count = 1
    options = ['name', 'event_title', 'event_date','event_location']
    length = len(options)

    for person in attendees:
        message = template_content
        for n in range (0,length):
            try:
                x = person[options[n]]
                if x is None:
                    raise KeyError     
            except KeyError:
                x = "N/A"
            message = message.replace('{'+ options[n] + '}', x)

        printer = message

        printerPath = f"output_{count}.txt"
        with open(printerPath, "w", encoding="utf-8") as f:
            f.write(printer)

        count += 1