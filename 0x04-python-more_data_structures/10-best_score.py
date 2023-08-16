#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    ret = 0
    name = ""
    for k, i in a_dictionary.items():
        if i > ret:
            ret = i
            name = k
    if ret == 0:
        return None
    else:
        return name
