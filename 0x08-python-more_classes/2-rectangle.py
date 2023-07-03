#!/usr/bin/python3

"""A class that defines a rectangle"""


class Rectangle:
    """This class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializing this rectangle class

        Args:
            width (int): Represents the width of the rectangle
            height (int): Represents the height of the rectangle

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
