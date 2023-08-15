#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    i = (len(my_list) - 1)
    t = int, float
    while i > -1:
        if isinstance(my_list[i], t):
            print("{:d}".format(my_list[i]))
        else:
            message = "Traceback (most recent call last):"
            print(f"{message}")
            return
        i -= 1

list = [1, 2, "H", 9]
print_reversed_list_integer(list)
