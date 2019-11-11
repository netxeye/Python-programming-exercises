#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'No pain no Gain'


def question15_compute(input_str):
    'Question 15'
    if len(input_str) == 1 and input_str.isdigit():
        return str(int(input_str) + int(input_str * 2) +
                   int(input_str * 3) + int(input_str * 4))
    else:
        raise ValueError


print(question15_compute(input('Enter a digit: ')))
