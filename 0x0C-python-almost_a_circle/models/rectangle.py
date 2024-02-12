#!/usr/bin/python3
"""This module contains a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the right attributes."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getters:

    @property
    def width(self):
        """ Get width """
        return self.__width

    @property
    def height(self):
        """ Get height """
        return self.__height

    @property
    def x(self):
        """ Get x """
        return self.__x

    @property
    def y(self):
        """ Get y """
        return self.__y

    # Setters:

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an int")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an int")
        self.__y = value

    def area(self):
        """ Computes area of rectangle """
        return (self.__height * self.__width)
