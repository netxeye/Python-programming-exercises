#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question42_even_tuple(input_tuple):
    if not isinstance(input_tuple, tuple):
        raise ValueError('Exception: Function only accepts Tuple value')
    return tuple((x for x in input_tuple if x % 2 == 0))


print(question42_even_tuple(tuple(range(1, 11))))
