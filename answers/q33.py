#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question33_dict(start, end):
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise ValueError('Exception: Function only accpets integer value')
    return dict((x, x ** 2) for x in range(start, end))


print(question33_dict(1, 21))
