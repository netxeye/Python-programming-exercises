#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question39_expect_first_5(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: The function only accpets inetger')
    return [x ** 2 for x in range(start, end)][5:]


print(question39_expect_first_5(1, 20))
