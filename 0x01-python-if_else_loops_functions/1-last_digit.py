#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = int(str(number)[-1])
if last_dig > 5:
    p = 'and is greater than 5'
if last_dig == 0:
    p = 'and is 0'
if last_dig < 6 and last_dig != 0:
    p = 'and is less than 6 and not 0'
print(f'Last digit of {number} is {last_dig} \
        {p}')
