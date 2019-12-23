#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question38_last_5_elements(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: The function only accpts integer value')
    return [x ** 2 for x in range(start, end)][-5:]


print(question38_last_5_elements(1, 21))
