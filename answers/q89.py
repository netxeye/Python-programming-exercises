#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question89RemoveOddIdex(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    return [x for (i, x) in enumerate(lis) if i % 2 == 0]


def question89RemoveSome(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accpets list value')
    if len(lis) < 6:
        raise ValueError('Exception: Parameter lis has longer than 6')
    return [x for (i, x) in enumerate(lis) if i not in (0, 4, 5)]


print(question89RemoveOddIdex(list(range(100))))
print(question89RemoveSome(list(range(7))))
