#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for ind_c in my_string:
        if ind_c not in "Cc":
            new += ind_c
    return new
