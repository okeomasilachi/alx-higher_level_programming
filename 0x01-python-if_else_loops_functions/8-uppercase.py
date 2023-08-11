#!/usr/bin/python3
# converts a string to uppercase
def uppercase(name):
    i = 0
    while i < len(name):
        if ord(name[i]) >= 97 and ord(name[i]) <= 123:
            print("{}".format(chr(65 + (ord(name[i]) - 97))),
                  end="\n" if i == (len(name) - 1) else "")
        else:
            print(name[i], end="\n" if i == (len(name) - 1) else "")
        i += 1
