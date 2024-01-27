#!/usr/bin/python3
"""

This module prints out a name.

"""


def say_my_name(first_name, last_name=""):
    """ this function print out the name.
    Args:
        first_name(str): the first name
        last_name(str): the last name

    Returns:
        the full name.

    Raises:
        TypeError: if the args are not strings.

    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
