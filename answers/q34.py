#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question34(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: The function only accpets integer value')
    return list(dict((x, x ** 2) for x in range(start, end)).values())


print(question34(1, 21))
