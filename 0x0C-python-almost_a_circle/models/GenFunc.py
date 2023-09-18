#!/usr/bin/python3

"""model for general functions"""


def validate(value, name):
    """
    checks if a given value is of the correct type and within
    the specified range for a given name.

    Args:
      value: The value that needs to be validated. It can be
        any data type, but the function specifically checks
        if it is an integer.
      name: The `name` parameter is a string that represents
        the name of the value being validated. It is used in
        the error messages to provide more specific information
        about which value failed the validation.

    Returns:
      a boolean value. It returns True if all the conditions
      are met and the value is valid, and False if any of the
      conditions are not met and the value is invalid.
    """
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
        return False
    if value < 1 and name in ["width", "height"]:
        raise ValueError(f"{name} must be > 0")
        return False
    if value < 0 and name in ["x", "y"]:
        raise ValueError(f"{name} must be >= 0")
        return False
    else:
        return True


def myvars(obj, value=[]):
    """
    Takes an object as input and returns a dictionary
    containing the object's attributes and their
    corresponding values.

    Args:
      obj: An object or instance of a class.

    Returns:
      Dictionary containing the attributes and their
      values of the input object `obj`. If the input
      object is empty or `None`, an empty dictionary
      is returned.
    """
    if not obj:
        return {}
    else:
        att = {}
        if value is not None:
            for name in value:
                att[name] = getattr(obj, name)
        else:
            for key in dir(obj):
                if not key.startswith("_"):
                    att[key] = getattr(obj, key)

    return att


def create_dictionary(keys, values):
    """
    Creates a dictionary where the elements of `keys`
    are the keys and the elements of `values` are the
    corresponding values.

    Args:
      keys: A list of keys for the dictionary.
      values: The `values` parameter is a list of values
        that you want to assign to the keys in the dictionary.

    Returns:
      a dictionary that is created by pairing the elements of
      the `keys` list with the corresponding elements of the
      `values` list.
    """
    d = {}
    for i in range(min(len(keys), len(values))):
        d[keys[i]] = int(values[i])
    return d
