#! /usr/bin/env python3
#-*- coding: utf-8 -*-


def question23_square(number):
    try:
        return number ** 2
    except (ValueError , TypeError) as VE:
        print(r'You have to use digital', VE)
        return 0


print(question23_square(input('You will enter a string: ')))
print(question23_square(int(input('The number will conver to int: '))))
