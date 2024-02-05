#!/usr/bin/python3
""" Checking """


def is_same_class(obj, a_class):
    """ checking if its from a class or not. """
    if type(obj) == a_class:
        return True
    return False
