#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'No pain no gain'


def question14_counting(input_str):
    'Question 14'
    uppers, lowers = 0, 0
    for item in input_str:
        if item.isupper():
            uppers += 1
        elif item.islower():
            lowers += 1
    return {'UPPER CASE': str(uppers), 'LOWER CASE': str(lowers)}


for key, value in question14_counting(input('Enter a sentence :')).items():
    print(key, value)
