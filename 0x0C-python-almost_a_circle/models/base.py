#!/usr/bin/python3
""" This module acts like a base for other classes. """

class Base:
    """ Represent base for all classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base object and assign a unique ID if not provided. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
