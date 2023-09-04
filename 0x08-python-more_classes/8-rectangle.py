#!/usr/bin/python3

"""
Module that defines all possible methods for tha class Rectangle
"""


class Rectangle:
    """
    class Rectangle defines a rectangle class
    """

    """
    Public class attribute number_of_instances:
    Initialized to 0

    Incremented during each new instance instantiation
    Decremented during each instance deletion
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructs a new rectangle object with the specified width and height.
        Increament the number_of_instances by 1

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
            Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self._height * self._width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self._height == 0 or self._width == 0:
            return 0

        return 2 * (self._height + self._width)

    def __str__(self):
        """
        print() and str() should print the rectangle with the character #

        Returns:
            Non empty string if width or height is not 0
            empty string if width or height is 0
        """
        self.__string = ""
        if self._height == 0 or self._width == 0:
            return self.__string
        for i in range(self._height):
            for j in range(self._width):
                self.__string += str(Rectangle.print_symbol)
            if i != self._height - 1:
                self.__string += '\n'
        return self.__string

    def __repr__(self):
        """
        return a string representation of the rectangle to be able to
        recreate a new instance by using eval()

        Returns:
            string representation of the rectangle
            to recreate a new instance by using eval()
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """
        prints the message 'Bye rectangle...
        when a particular instance is being deleted'
        and decreament the number_of_instances by 1

        Returns:
            None
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area

        Args:
            rect_1: first case
            rect_2 second case

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle
            TypeError: If rect_2 is not an instance of Rectangle

        Returns:
            The biggests
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            elif rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
