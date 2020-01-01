#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import sample


def question85Sample(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    lis.remove(sample(lis, 1)[0])
    return lis


def question85SamplePop(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    lis.pop(sample(range(len(lis)), 1)[0])
    return lis


def question85DeleteEven(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    return [x for x in lis if x % 2 != 0]


print(question85Sample([x for x in range(25) if x % 3 == 0]))
print(question85SamplePop([x for x in range(25) if x % 3 == 0]))
print(question85DeleteEven([x for x in range(24)]))
