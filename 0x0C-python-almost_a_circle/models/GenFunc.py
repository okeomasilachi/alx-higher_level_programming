#!/usr/bin/python3

""""""


def validate(value, name):
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
    Takes an object as input and returns a dictionary containing the object's
    attributes and their corresponding values.

    Args:
      obj: An object or instance of a class.

    Returns:
      Dictionary containing the attributes and their values of the
      input object `obj`. If the input object is empty or `None`,
      an empty dictionary is returned.
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
    d = {}
    for i in range(min(len(keys), len(values))):
        d[keys[i]] = int(values[i])
    return d
