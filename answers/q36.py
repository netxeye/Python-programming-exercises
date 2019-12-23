#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question36_list(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: The function only accpets integer')
    return list(x ** 2 for x in range(start, end))


print(question36_list(1, 21))
