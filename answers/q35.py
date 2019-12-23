#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question35(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: The function only accpets integer value')
    return list(dict((x, x ** 2) for x in range(start, end)).keys())


print(question35(1, 21))
