#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def question30_compare_length(string1, string2):
    if (not isinstance(string1, str) or (not isinstance(string2, str))):
        raise TypeError('Exception: The function only accpet String')
    if len(string1) > len(string2):
        return string1
    elif len(string1) == len(string2):
        return string1 + ' ' + string2
    else:
        return string2


input_str1 = input('Please enter the first value: ')
input_str2 = input('Please enter the second value: ')
print(question30_compare_length(input_str1, input_str2))
try:
    question30_compare_length(44, 55)
except TypeError as message:
    print(message)
