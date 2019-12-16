#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question28_sum(num1_str, num2_str):
    if (not isinstance(num1_str, str)) or (not isinstance(num2_str, str)):
        raise ValueError('Exception: question28_sum only appect String')
    try:
        return int(num1_str) + int(num2_str)
    except ValueError as message:
        print('Exception:', message)
        return 0


number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
try:
    print(question28_sum(int(number1), int(number2)))
except ValueError as message:
    print('Exception: ', message)
print(question28_sum(number1, number2))
question28_sum('abc', 'sss')
