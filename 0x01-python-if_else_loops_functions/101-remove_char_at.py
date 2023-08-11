#!/usr/bin/python3
def remove_char_at(strs, n):
    if n < 0 or n >= len(strs):
        return strs
    sen = ""
    for i in range(len(strs)):
        if i != n:
            sen += strs[i]
    return sen
