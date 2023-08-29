#!/usr/bin/python3

my_module = "3-square"
my_function = "__init__"
MyClass = "Square"

print(__import__(my_module).__doc__)
print(__import__(my_module).Square.__doc__)
print(__import__(my_module).Square.__init__.__doc__)
print(__import__(my_module).Square.area.__doc__)
