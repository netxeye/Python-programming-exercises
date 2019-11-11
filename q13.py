#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'I love Lucie and Luna'


def question13_counting(str_input):
    'Question13'
    letters, digits = 0, 0
    for item in str_input:
        if item.isalpha():
            letters += 1
        elif item.isdigit():
            digits += 1
    return {'LETTERS': str(letters), 'DIGITS': str(digits)}


for key, value in question13_counting(input('Enter a sentence: ')).items():
    print(key, value)
