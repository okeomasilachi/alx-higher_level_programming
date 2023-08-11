#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
val = str(number)[-1]
if number < 0:
    val = int(val)
    val = val - (val * 2)
else:
    val = int(val)
print(f"Last digit of {number} is {val}", end=" ")
if val > 5:
    print("and is greater than 5")
elif val == 0:
    print("and is 0")
elif val != 0 and val < 6:
    print("and is less than 6 and not 0")
