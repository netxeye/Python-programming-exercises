#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint, sample


def question76Random5(start, end):
    if (
        (not isinstance(start, int))
        or
        (not isinstance(end, int))
       ):
        raise ValueError('Exception: Function only accepts integer value')
    __random_list = list()
    for times in range(5):
        __random_list.append(randint(start, end))
    return __random_list


def question76Random5Better(start, end):
    if (
        (not isinstance(start, int))
        or
        (not isinstance(end, int))
       ):
        raise ValueError('Exception: Function only accepts integer value')
    return sample(range(start, end), 5)


print(question76Random5(100, 201))
print(question76Random5Better(100, 201))
