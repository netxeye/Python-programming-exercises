#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question86Delete5_7(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accpets list value')
    return [x for x in lis
            if x % 5 == 0
            and
            x % 7 == 0
            ]


print(question86Delete5_7(list(range(120))))
