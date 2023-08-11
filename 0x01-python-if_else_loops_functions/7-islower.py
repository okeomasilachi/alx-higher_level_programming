#!/usr/bin/python3
# checks if a chracter is an upper case letter
def islower(c):
    val = ord(c)
    if val >= 97 and val <= 123:
        return True
    else:
        return False
