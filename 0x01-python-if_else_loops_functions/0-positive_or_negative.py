#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0 or number < -1 or number < -5:
    print("{} is negative".format(number))
elif number == 0:
    print("{} is zero".format(number))
elif number > 0 or number > 1 or number > 100:
    print("{} is positive".format(number))
