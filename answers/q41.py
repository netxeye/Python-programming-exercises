#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question41_half_half(tuple_input):
    if not isinstance(tuple_input, tuple):
        raise ValueError('Exception: The function only accpets Tuple')
    print(tuple_input[:int(len(tuple_input) / 2)])
    print(tuple_input[int(len(tuple_input) / 2):])


question41_half_half(tuple(range(1, 11)))
