#!/usr/bin/python3
for pos in range(122, 96, -1):
    if pos % 2 == 0:
        print("{0}".format(chr(pos)), end="")
    else:
        print("{0}".format(chr(pos).upper()), end="")
