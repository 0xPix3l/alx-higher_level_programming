#!/usr/bin/python3


""" This module for make reading easier. """


def text_indentation(text):
    """ making reading easier.

    Args:
            text: taking a chr

    Raises:
            TypeError: must be a string

    Returns:
            two lines after every ['.', '?', ':']

    """
    alist = ['.', '?', ':']
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    else:
        for char in alist:
            text = text.replace(char, char + 2 * '\n')
    print(text)
