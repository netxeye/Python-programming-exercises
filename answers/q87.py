#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question87RemoveSome(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    if len(lis) < 7:
        raise ValueError('Exception: Parameter lis must lenger than 7')
    return [x for (i, x) in enumerate(lis) if i not in (0, 3, 5, 7)]


def question87RemoveSome2(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    if len(lis) < 7:
        raise ValueError('Exception: Parameter lis must lenger than 7')
    return [x for (i, x) in enumerate(lis) if i % 2 != 0]


print(question87RemoveSome(list(range(10))))
print(question87RemoveSome2(list(range(10))))
