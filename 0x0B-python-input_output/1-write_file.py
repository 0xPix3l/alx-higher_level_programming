#!/usr/bin/python3
""" Defines a function that write to a file."""


def write_file(filename="", text=""):
	"""Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)
        print(len(text))
