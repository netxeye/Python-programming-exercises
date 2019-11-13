#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'Do the best'
from math import sqrt


def question16_sqrt_odds(input_sequence):
    output_list = list()
    for item in input_sequence:
        if isinstance(item, str) and item.isdigit():
            if int(item) % 2 != 0:
                output_list.append(str(sqrt(int(item))))
        elif isinstance(item, int):
            if item % 2 != 0:
                output_list.append(str(sqrt(item)))
    return output_list


def question16_square_odds(input_sequence):
    output_list = list()
    for item in input_sequence:
        if isinstance(item, str) and item.isdigit():
            if int(item) % 2 != 0:
                output_list.append(str(int(item) ** 2))
        elif isinstance(item, int):
            if item % 2 != 0:
                output_list.append(str(item ** 2))
    return output_list


print(','.
      join(question16_sqrt_odds(
           input('Please enter sequence of comma-separated number:').
           split(','))))
print(','.
      join(question16_square_odds(
           input('Please enter sequence of comma-separated number: '))))
