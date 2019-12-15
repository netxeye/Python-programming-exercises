#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question26_sum(num1, num2):
    if (not isinstance(num1, int)) or (not isinstance(num2, int)):
        raise ValueError('Function only accpet integer')
    return num1 + num2


number1 = input('Please input the frist number')
number2 = input('Please input the second number')
try:
    print(question26_sum(number1, number2))
except ValueError as message:
    print('Exception: ', message)
print(number1, '+' , number2, '=', question26_sum(int(number1), int(number2)))
