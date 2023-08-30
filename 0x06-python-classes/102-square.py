#!/usr/bin/python3

""" defines a square by: (based on 4-square.py) """


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
        if not isinstance(size, int or float):
            raise TypeError("size must be a number")
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
        if not isinstance(value, int or float):
            raise TypeError("size must be a number")
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

    def __eq__(self, other):
        """Compare two squares for equality.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        """Compare two squares for inequality.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if the squares are not equal
                  False otherwise.
        """
        if self.area() != other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        """Compare two squares for greater than.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if the first square is greater than the second
                  False otherwise.
        """
        if self.area() > other.area():
            return True
        else:
            return False

    def __ge__(self, other):
        """Compare two squares for greater than or equal to.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if the 1st square is greater than or equal to the second
                  False otherwise.
        """
        if self.area() >= other.area():
            return True
        else:
            return False

    def __lt__(self, other):
        """Compare two squares for less than.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if the first square is less than the second
                  False otherwise.
        """
        if self.area() < other.area():
            return True
        else:
            return False

    def __le__(self, other):
        """Compare two squares for less than.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if the first square is less than the second
                  False otherwise.
        """
        if self.area() <= other.area():
            return True
        else:
            return False
