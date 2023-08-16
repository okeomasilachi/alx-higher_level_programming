#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not set_1 or not set_2:
        return set()
    else:
        return set_1 ^ set_2
