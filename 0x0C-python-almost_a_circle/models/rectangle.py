#!/usr/bin/python3

"""Holds the model for the Rectangle class"""


try:
    from .base import Base
except Exception:
    from base import Base
try:
    from .GenFunc import validate, myvars
except Exception:
    from GenFunc import validate, myvars


class Rectangle(Base):
    """
    The Rectangle class is a subclass of the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes an object with width, height, x, y, and id attributes,
        after validating the input values.

        Args:
          width: The width parameter represents the width of an object.
            It is used to specify the horizontal size of the object.
          height: The `height` parameter represents the height of an object.
            It is used to set the height of object in the `__init__` method.
          x: The parameter "x" represents the x-coordinate of the object's
            position. It determines the horizontal position of the object on
            a coordinate plane. Defaults to 0
          y: The parameter "y" represents the y-coordinate of the object's
            position. It determines the vertical position of the object on a
            coordinate plane. Defaults to 0
          id: The `id` parameter is an optional parameter that represents
            the identifier of the object. It is used to uniquely identify an
            instance of the class. If no `id` is provided, it will be set to
            `None`.
        """
        if not validate(width, "width"):
            pass
        elif not validate(height, "height"):
            pass
        elif not validate(x, "x"):
            pass
        elif not validate(y, "y"):
            pass
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
            super().__init__(id)

    @property
    def width(self):
        """
        The function returns the width attribute of an object.

        Returns:
          The width of the object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The function sets the width attribute of an object if the
        value is valid.

        Args:
          value: The value parameter represents the width value that
          is being passed to the width method.
        """
        if validate(value, "width"):
            self.__width = value

    @property
    def height(self):
        """
        The function returns the height of an object.

        Returns:
          The height of the object.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The function sets the height attribute of an object if
        the value is valid.

        Args:
          value: The value parameter represents the height value
            that is being passed to the height method.
        """
        if validate(value, "height"):
            self.__height = value

    @property
    def x(self):
        """
        The function returns the value of the private variable __x.

        Returns:
          The method x is returning the value of the attribute __x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        The function sets the value of the private variable __x if
        it passes the validation check.

        Args:
          value: The value parameter is the value that we want to
            assign to the private attribute __x.
        """
        if validate(value, "x"):
            self.__x = value

    @property
    def y(self):
        """
        The function returns the value of the private variable __y.

        Returns:
          The method is returning the value of the private
          variable `__y`.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the value of the private attribute "__y" if the input
        value passes a validation check.

        Args:
          value: The value parameter is the value that you want to
          set for the attribute "y".
        """
        if validate(value, "y"):
            self.__y = value

    def area(self):
        """
        The above function calculates the area of a rectangle.

        Returns:
          The area of the rectangle, which is calculated by
          multiplying the height and width of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """
        The function displays a rectangle made of "#" characters,
        with the option to specify the position and size of the
        rectangle.
        """
        if self.__y > 0:
            for i in range(self.__y):
                print(" ")
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        The function returns a string representation of a Rectangle object,
        including its id, position, width, and height.

        Returns:
          The `__str__` method is returning a string representation of a
          Rectangle object. The string includes the object's id, x and y
          coordinates, width, and height.
        """
        ret = f"[Rectangle] ({self.id})"\
              f" {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return ret

    def update(self, *args, **kwargs):
        """
        The `update` function updates the attributes of an object based
        on either positional arguments or keyword arguments.
        """
        if args:
            self.id = args[0]
            for name, value in zip(["width", "height", "x", "y"], args[1:]):
                if validate(value, name):
                    setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in ["id", "width", "height", "x", "y"]:
                    if name not in ["width", "height", "x", "y"]:
                        setattr(self, name, value)
                    else:
                        if validate(value, name):
                            setattr(self, name, value)

    def to_dictionary(self):
        """
        The function "to_dictionary" returns a dictionary containing the
        values of the specified attributes.

        Returns:
          a dictionary with the keys "id", "width", "height", "x", and "y".
          The values of these keys are the corresponding values of the
          variables "id", "width", "height", "x", and "y" in the object.
        """
        return myvars(self, ["id", "width", "height", "x", "y"])
