#!/usr/bin/python3

"""
This file defines a square by:

* A class called `Square` that represents a square.
* The `Square` class has the following attributes:
    * `__size`: The size of the square's sides.
    * `__position`: The position of the square, which is a tuple of
                    two positive integers.
* The `Square` class has the following methods:
    * `__init__(self, size, position)`: Initialize a square with the
                                        given size and position.
    * `size(self)`: Get the square's size.
    * `size(self, value)`: Set the square's size.
    * `position(self)`: Get the square's position.
    * `position(self, value)`: Set the square's position.
    * `area(self)`: Get the area of the square.
    * `my_print(self)`: Print the square.
"""


class Square:
    """A class representing a square. """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with the given size and position.

        Args:
            size (int, optional): The size of the square's sides. Default is 0.
            position (tuple, optional): The position of the square,
            which is a tuple of two positive integers. Default is (0, 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
            TypeError: if not tuple of 2 positive integers.
        """
        # Check if the size is an integer.
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  # The size of the square is private.

        # Check if the position is a tuple of two positive integers.
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 "
                            "positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 "
                            "positive integers")
        elif position[0] and position[1] < 0:
            raise TypeError("position must be a tuple of 2 "
                            "positive integers")
        else:
            # The position of the square is private.
            self.__position = position

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

    # Define a property for the position attribute.
    @property
    def position(self):
        """Get the square's position."""
        return (self.__position)

    # Define a setter method for the position attribute.
    @position.setter
    def position(self, value):
        """Set the square's position.

        Args:
            value (int): The new position of the square.

        Raises:
            TypeError: if not tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 "
                            "positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 "
                            "positive integers")
        elif value[0] and value[1] < 0:
            raise TypeError("position must be a tuple of 2 "
                            "positive integers")
        else:
            self.__position = value  # The position of the square is private.

    def area(self):
        """Get the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square.

        If the size is 0, print an empty line. Otherwise, print a line of #'s
        for each side of the square.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] > 0:
                    print("_" * self.__position[1], end="")
                else:
                    print("_" * self.__position[0], end="")
                print("#" * self.__size)
