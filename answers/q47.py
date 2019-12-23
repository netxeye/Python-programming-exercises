#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question47_filter(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: Function only accepts integer value')
    return list(filter(lambda x: x % 2 == 0, range(start, end)))


print(question47_filter(1, 21))


def question47_even(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: Function only accpets integer value')
    return [x for x in range(start, end) if x % 2 == 0]


print(question47_even(1, 21))
