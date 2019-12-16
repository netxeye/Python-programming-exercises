#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Question 10
'''


def question10_remove_duplicate_sort(input_data_list):
    'Question 10 function'
    try:
        return sorted(set(input_data_list))
    except (TypeError, AttributeError) as error_message:
        print('Incorrect:', error_message)


INPUT_DATA_SEQUENCE = list()
while True:
    INPUT_DATA = input('Enter a sequence of whitespace separated words (Enter'
                       ' empty will exit): ')
    if INPUT_DATA:
        INPUT_DATA_SEQUENCE += INPUT_DATA.split()
    else:
        break
for item in question10_remove_duplicate_sort(INPUT_DATA_SEQUENCE):
    print(item, end=' ')
