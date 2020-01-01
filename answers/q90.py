#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question90Remve24(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    return [x for x in lis if x != 24]


print(question90Remve24(list(range(25))))
