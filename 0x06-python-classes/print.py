#!/usr/bin/python3

my_module = "1-square"
my_function = "__init__"
MyClass = "Square"

print(__import__(my_module).__doc__)
print(__import__(my_module).Square.__doc__)
print(__import__(my_module).__init__.__doc__)
print(__import__(my_module).Square.__init__.__doc__)
