#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import shuffle


def question82Shuffle(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    shuffle(lis)
    return lis


print(question82Shuffle(list(range(100))))
