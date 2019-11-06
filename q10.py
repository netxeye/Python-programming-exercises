#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question10_remove_duplicate_sort(input_data):
    try:
        return sorted(set(input_data))
    except (TypeError, AttributeError) as es:
        print('Incorrect:', es)


input_data_sequence = list()
while True:
    input_data = input('Enter a sequence of whitespace separated words (Enter'
                       ' empty will exit): ')
    if input_data:
        input_data_sequence += input_data.split()
    else:
        break
for item in question10_remove_duplicate_sort(input_data_sequence):
    print(item, end=' ')
