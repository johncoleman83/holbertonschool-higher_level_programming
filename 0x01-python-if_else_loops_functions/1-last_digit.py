#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = ["Last digit of", "is", "and is greater than 5", "and is 0",
     "and is less than 6 and not 0"]
n = number % 10
print(s[0], number, s[1], n, s[3] if n == 0 else s[2] if n > 5 else s[4])
