#!/usr/bin/python3
""" This module acts like a base for other classes. """


class Base:
    """ Represent base for all classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
