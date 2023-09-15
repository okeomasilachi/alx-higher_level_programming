#!/usr/bin/python3

""""""


try:
    from .rectangle import Rectangle
except:
    from rectangle import Rectangle
try:
    from .GenFunc import validate, myvars
except:
    from GenFunc import validate, myvars


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        i = 0
        ret = super().__str__().replace("Rectangle", "Square")
        while ret[i] != "/":
            i -= 1
        return ret[:i]

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        if validate(value, "width"):
            self.update(width=value, height=value)

    def update(self, *args, **kwargs):
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
        return myvars(self, ["id", "size", "x", "y",])
