#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    tmp = []

    for i in range(list_length):
        try:
            tmp.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            tmp.append(0)
        except ZeroDivisionError:
            print("division by 0")
            tmp.append(0)
        except IndexError:
            print("out of range")
            tmp.append(0)
        finally:
            continue
    return tmp
