#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question27_convert(integer):
    if not isinstance(integer, int):
        raise ValueError('Qustion27 only accept integer')
    return str(integer)


number = input('Enter a number: ')
try:
    print(question27_convert(number))
except ValueError as message:
    print('Exception: ', message)
print(question27_convert(int(number)))
