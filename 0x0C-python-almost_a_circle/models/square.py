#!/usr/bin/python3

"""
Module that defines a Square object.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a Square class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square object.

        Args:
           size (int): The size of the square.
           x (int): The x-coordinate of the square.
           y (int): The y-coordinate of the square.
           id (int): The unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """
        Gets the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
           value (int): The size to assign to the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square object.

        Args:
           *args: List of arguments.
           **kwargs: Dictionary with arguments.
        """
        dict_order = ['id', 'size', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """
        Returns a dictionary with the attributes of the square object.
        """
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
