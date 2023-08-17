#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = {}
    if not a_dictionary:
        return a_dictionary
    elif not value:
        return a_dictionary
    for i, k in a_dictionary.items():
        print(i, 	k)
    a_dictionary = new
    return a_dictionary
        
