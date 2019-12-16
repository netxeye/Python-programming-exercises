#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question8_alph_sequence(sequence):
    return sorted(sequence)


input_data = input('Please a comma separated sequence: ')
print(list(question8_alph_sequence(input_data.split(','))))
