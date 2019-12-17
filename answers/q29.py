#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question29_concatenate(string1, string2):
    if (not isinstance(string1, str)) or (not isinstance(string2, str)):
        raise TypeError('Exception: Function only accpets String')
    return string1 + string2


input_str1 = input('Enter the first valuse: ')
input_str2 = input('Enter the second valuse: ')
try:
    print(question29_concatenate(int(input_str1), input_str2))
except (TypeError, ValueError) as message:
    print(message)
print(question29_concatenate(input_str1, input_str2))
