#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
# To ge last digit
last_digit = abs(number) % 10
"""
This code is to check 
1. the last number and
then for last number
1. wether the last digit is greater than 5
2. wether the last digit is 0
3. wether the last digit is less than 6 and not 0
"""
if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")

if last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")

if (last_digit < 6) and (last_digit != 0):
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
