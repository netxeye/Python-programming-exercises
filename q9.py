#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question9_upper(input_data):
    try:
        return input_data.upper()
    except AttributeError as ae:
        print('Incorrect type! Only accpect String', ae)


def question9_sequence_upper(input_data):
    try:
        copy_input_data = []
        for charter in input_data:
            copy_input_data.append(charter.upper())
    except AttributeError as ae:
        print('Incorrect tyep! Only accpet String', ae)
    return copy_input_data


input_data = input('Please enter String, we try to capitalized it: ')
print(question9_upper(input_data))
question9_upper({})
input_data_sequence = list()
while True:
    input_data = input('Please enter list of string, we try to capilized'
                       'them (enter empty value will exit):')
    if input_data:
        input_data_sequence.append(input_data)
    else:
        break
print(question9_sequence_upper(input_data_sequence))
for charter in question9_sequence_upper(input_data_sequence):
    print(charter)
