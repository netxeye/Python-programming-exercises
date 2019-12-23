#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question37_5_elements(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: The function only accpets integer')
    return [x ** 2 for x in range(start, end)][:5]


print(question37_5_elements(1, 21))
