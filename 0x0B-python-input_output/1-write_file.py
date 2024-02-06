#!/usr/bin/python3
""" Defines a function that write to a file."""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)
        return(len(text))
