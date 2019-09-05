#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def factorial(n):
    if n == 1:
        return n
    else:
        return factorial(n - 1) * n


input_data = input('Please enter a number, for example 8:')
check_list = tuple(map(str, range(0, 10)))
while True:
    if input_data in check_list and input_data:
        print(str(factorial(int(input_data))) + ',')
        break
    else:
        print('please enter number from 0 -9.')
        input_data = input('Please enter a number, for example 8:')
