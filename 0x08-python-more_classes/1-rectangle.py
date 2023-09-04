#!/usr/bin/python3

"""
Module that defines all possible methods for tha class Rectangle
"""


class Rectangle:
    """
    class Rectangle defines a rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Constructs a new rectangle object with the specified width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.

        Raises:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is less than 0.
        """

        if not isinstance(width, int):  # Check if `width` is an integer.
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):  # Check if `height` is an integer.
            raise TypeError("height must be an integer")
        elif width < 0:  # Check if `width` is greater than or equal to 0.
            raise ValueError("width must be >= 0")
        elif height < 0:  # Check if `height` is greater than or equal to 0.
            raise ValueError("height must be >= 0")
        else:
            # Set the private attributes `_width` and `_height`
            # to `width` and `height` respectively.
            self._width = width
            self._height = height

    @property
    def width(self):
        """
        Returns the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value: The new width of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):  # Check if `value` is an integer.
            raise TypeError("width must be an integer")
        elif value < 0:  # Check if `value` is greater than or equal to 0.
            raise ValueError("width must be >= 0")
        else:
            # Set the private attribute `_width` to `value`.
            self._width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value: The new height of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """

        if not isinstance(value, int):  # Check if `value` is an integer.
            raise TypeError("height must be an integer")
        if value < 0:  # Check if `value` is greater than or equal to 0.
            raise ValueError("height must be >= 0")
        else:
            # Set the private attribute `_height` to `value`.
            self._height = value
