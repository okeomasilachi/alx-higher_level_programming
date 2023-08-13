#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for ind_c in my_string:
        if ind_c != 'c' and ind_c != 'C':
            new += ind_c
    return new
