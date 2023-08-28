#!/usr/bin/python3

if __name__ == "__main__":
    def safe_print_list(my_list=[], x=0):
        ct = 0
        try:
            for i in range(x):
                print(my_list[i], end="")
                ct += 1
        except IndexError as er:
            print("\nError:", er, end="")
        finally:
            print()
            return ct
