#!/usr/bin/python3

"""Define a class square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """init a new square

        args:
            size (int): the size of the new one
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
