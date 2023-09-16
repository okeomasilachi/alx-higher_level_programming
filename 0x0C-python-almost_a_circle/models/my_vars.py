#!/usr/bin/python3

"""
"""
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




class person:
    def __init__(self, first_name="", last_name="", age=00):
        self.age = age
        self.last_name =last_name
        self.first_name = first_name
    def __str__(self):
        return f"first name: {self.first_name}\nlast name: {self.last_name}\nage: {self.age}"


p1 = person("Okeomasilachi", "Onyedibia", 67)

print(myvars(p1))