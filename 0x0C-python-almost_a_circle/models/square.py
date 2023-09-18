#!/usr/bin/python3

"""Holds the model for the Square class"""


try:
    from .rectangle import Rectangle
except Exception:
    from rectangle import Rectangle
try:
    from .GenFunc import validate, myvars
except Exception:
    from GenFunc import validate, myvars


class Square(Rectangle):
    """
    The class Square is a subclass of the class Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        The above function is a constructor that initializes an object
        with a given size, position, and optional id.

        Args:
          size: The size parameter represents the size of an object.
            It is used to specify the width and height of the object.
            In this case, the object is being initialized with a square
            shape, so the width and height are both set to the value
            of size.
          x: The x-coordinate of the object's position. It represents the
            horizontal position of the object on a 2D plane. By default,
            it is set to 0. Defaults to 0
          y: The `y` parameter represents the y-coordinate of the object's
            position. It determines the vertical position of the object on
            a coordinate plane. Defaults to 0
          id: The `id` parameter is an optional parameter that represents
            the unique identifier for an object. It is used to distinguish
            between different instances of the same class. If no `id` is
            provided, it will default to `None`.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overrides the __str__ method of a class to replace the word
        "Rectangle" with "Square" in the string representation of
        the object.

        Returns:
          The code is returning a modified string representation of the
          object. It replaces the word "Rectangle" with "Square" in the
          original string representation and removes everything after the
          first forward slash ("/").
        """
        i = 0
        ret = super().__str__().replace("Rectangle", "Square")
        while ret[i] != "/":
            i -= 1
        return ret[:i]

    @property
    def size(self):
        """
        The size function returns the width of an object.

        Returns:
          The width of the object.
        """
        return super().width

    @size.setter
    def size(self, value):
        """
        The function updates the width and height of an object if the value
        passed is valid.

        Args:
          value: The value parameter represents the size value that will
          be used to update the width and height attributes of the object.
        """
        if validate(value, "width"):
            self.update(width=value, height=value)

    def update(self, *args, **kwargs):
        """
        The `update` function updates the attributes of an object based
        on the provided arguments or keyword arguments.
        """
        if args:
            self.id = args[0]
            for name, value in zip(["size", "x", "y"], args[1:]):
                if validate(value, name):
                    if name == "size":
                        super().update(width=value, height=value)
                    else:
                        setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in ["id", "size", "x", "y"]:
                    if name not in ["size", "x", "y"]:
                        setattr(self, name, value)
                    else:
                        if validate(value, name):
                            if name == "size":
                                super().update(width=value, height=value)
                            else:
                                setattr(self, name, value)

    def to_dictionary(self):
        """
        The function "to_dictionary" returns a dictionary containing the
        values of the "id", "size", "x", and "y" variables.

        Returns:
          a dictionary with keys "id", "size", "x", and "y". The values of
          these keys are the corresponding values of the variables "id",
          "size", "x", and "y" in the object.
        """
        return myvars(self, ["id", "size", "x", "y",])
