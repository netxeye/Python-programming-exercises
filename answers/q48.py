#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question48_map(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: Function only accepts integer value')
    return list(map(lambda x: x ** 2, range(start, end)))


def question48_square(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: Function only accepts integer value')
    return [x ** 2 for x in range(start, end)]


print(question48_map(1, 21))
print(question48_square(1, 21))
