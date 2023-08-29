#!/usr/bin/python3

""" defines a square by: (based on 2-square.py) """


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square's sides.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """
    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size (int, optional): The size of the square's sides. Default is 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  # The size of the square is private.

    # Define a property for the size attribute.
    @property
    def size(self):
        """Get the square's size."""
        return (self.__size)

    # Define a setter method for the size attribute.
    @size.setter
    def size(self, value):
        """Set the square's size.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  # The size of the square is private.

    def area(self):
        """Get the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
