import random
number = random.randint(-10000, 10000)
num = None

if number < 0:
    num = -abs(int(str(number)[-1]))
else:
    num = int(str(number)[-1])
if num > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, num))
elif num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
elif num < 6 and not 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, num))
