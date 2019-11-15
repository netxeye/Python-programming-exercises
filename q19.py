#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from operator import itemgetter


def question19_sort(sequence_tuple_value):
    return sorted(sequence_tuple_value, key=lambda x: (x[0], x[1], x[2]))


def question19_create_tuple(list_value):
    return (list_value[0], int(list_value[1]), int(list_value[2]))


list_data = list()
while True:
    input_date = input('Enter valuse separated by comma:(Empty value exit) ')
    if input_date:
        list_data.append(question19_create_tuple(input_date.split(',')))
    else:
        break
print(question19_sort(list_data))
print(sorted(list_data, key=itemgetter(0, 1, 2)))
