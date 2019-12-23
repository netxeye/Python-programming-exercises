#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question40_tuple(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: The fucntion only accpets inetger')
    return tuple((x ** 2 for x in range(start, end)))


print(question40_tuple(1, 21))
