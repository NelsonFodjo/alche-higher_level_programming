#!/usr/bin/python3
"""Module that defines a Square class with printing functionality."""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance with an optional size parameter."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the hash character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.size)
