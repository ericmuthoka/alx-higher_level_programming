#!/usr/bin/python3

"""
Square Module
"""


class Square:
    """
    Square Class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance
        Args:
            size (int): The size of the square (default 0)
            position (tuple): The position of the square (default (0, 0))
        Raises:
            TypeError: If size isnt integer or pos isnt a tuple of 2 +ve ints
            ValueError: If size or position values are less than 0
        """
        self.__size = 0
        self.__position = (0, 0)
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square
        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        Args:
            value (int): The size of the square
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square
        Returns:
            tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square
        Args:
            value (tuple): The position of the square
        Raises:
            TypeError: If value is not a tuple of 2 positive integers
            ValueError: If value values are less than 0
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#'
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
