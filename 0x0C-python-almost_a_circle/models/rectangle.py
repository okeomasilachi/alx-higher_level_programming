#!/usr/bin/python3

""""""


try:
    from .base import Base
except:
    from base import Base
try:
    from .GenFunc import validate, myvars
except:
    from GenFunc import validate, myvars


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
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
        return self.__width

    @width.setter
    def width(self, value):
        if validate(value, "width"):
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if validate(value, "height"):
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if validate(value, "x"):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if validate(value, "y"):
            self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        if self.__y > 0:
            for i in range(self.__y):
                print(" ")
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        ret = f"[Rectangle] ({self.id})"\
                f" {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return ret

    def update(self, *args, **kwargs):
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
        return myvars(self, ["id", "width", "height", "x", "y",])
