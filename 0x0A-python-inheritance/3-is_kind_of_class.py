#!/usr/bin/python3
""" instance or not. """


def is_kind_of_class(obj, a_class):
    """ Returns of it is a subclass or not. """
    if isinstance(obj, a_class):
        return True
    return False
