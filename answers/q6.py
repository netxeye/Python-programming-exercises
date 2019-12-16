#! /bin/env python3
# -*- coding: utf-8 -*-
import math

def question_def(input_seq):
    result_seq = list()
    for result in input_seq:
        try:
            result_seq.append(int(math.sqrt((2 * 50 * float(result)) / 30)))
        except ValueError as VE:
            print('Incorrect Type for INT', VE)
    return result_seq

try:
    input_line = input('Enter sequence number in a comma-separated: ').split(sep=',')
except TypeError as TE:
    print('Incorrect Type', TE)
print(question_def(input_line))
