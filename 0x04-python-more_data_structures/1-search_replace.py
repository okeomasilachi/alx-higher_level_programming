#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ret = []
    if not my_list:
        return ret
    for i in my_list:
        if i is search:
            ret.append(replace)
        else:
            ret.append(i)
    return ret
