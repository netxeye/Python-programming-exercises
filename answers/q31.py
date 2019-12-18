#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question31_determate_even_odd(integer):
    if not isinstance(integer, int):
        raise TypeError('Exception: The function only accept Integer value')
    if integer % 2 == 0:
        return 'It is an even number'
    else:
        return 'It is an odd number'


try:
    print(question31_determate_even_odd(input('Enter an integer value: ')))
except TypeError as message:
    print(message)
try:
    print(question31_determate_even_odd(int(input('Enter an integer value: '))))
except ValueError as message:
    print(message)
