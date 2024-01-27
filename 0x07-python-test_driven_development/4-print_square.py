#!/usr/bin/python3

""" This module for printing square in the form of hashes '#' """


def print_square(size):
    """ This function prints out a square in the form of hash symbols.

    Args:
        size (int): The number of rows and columns of the square.

    Raises:
        TypeError: Size must be an integer.
        ValueError: Size can't be zero.
        ValueError: Size can't be a float less than 1.

    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float):
        raise ValueError('size must be an integer or a float >= 1')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print("")
