#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """safe_print_list

    Args:
        my_list (list, optional): [The list to print]. Defaults to [].
        x (int, optional): [number of element to print from the list]. Defaults to 0.

    Returns:
        [int]: [Actual number of items printed]
    """
    ct = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            ct += 1
        except IndexError as er:
            continue
    print()
    return ct
