#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'Working hard for my family'


def queston11_input_sequence(input_sequence):
    'Question 11 '
    return [item for item in input_sequence if int(item, base=2) % 5 == 0]


SEQUENCE = input('Enter comma sequence 4 digit: ').split(',')
for item in queston11_input_sequence(SEQUENCE):
    print(item)
