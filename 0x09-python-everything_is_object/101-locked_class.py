#!/usr/bin/python3

"""
class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new
instance attributes, except if the new instance attribute
is called first_name.
"""


class LockedClass:
    """
    LockedClass.

    A class that prevents the user from dynamically
    creating new instance attributes, except if the new
    instance attribute is called first_name.

    Attributes:
        __slots__: A special attribute that lists the names
                    of the allowedinstance attributes.
                    In this case, we have set __slots__ to an
                    empty list, which means that no new instance
                    attributes are allowed.

        __setattr__: A special method that is called whenever
                    an attribute is assigned to an object. In
                    this case, we have overridden the __setattr__
                    method to check if the attribute name is "first_name".
                    If it is, then we allow the attribute to be assigned.
                    Otherwise, we raise an `AttributeError` exception.
    """
    def __setattr__(self, nm, value):
        """
        The function that does and handle the logic
        """
        if nm == "first_name":
            super().__setattr__(nm, value)
        else:
            raise AttributeError(f"'{self.__class__.__name__}'"
                                 f" object has no attribute '{nm}'")
