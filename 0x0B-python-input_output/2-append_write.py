#!/usr/bin/python3
""" appends to a text. """


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='UTF-8') as f:
        f.write(text)
        return len(text)
