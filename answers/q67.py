#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question67_even(n):
    if not isinstance(n, int):
        raise ValueError('Exception: Function only accepts integer value')
    return ', '.join([str(x) for x in range(n + 1) if x % 2 == 0])


print(question67_even(10))
