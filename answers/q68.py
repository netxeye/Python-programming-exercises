#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question68_divis_5_7(n):
    if not isinstance(n, int):
        raise ValueError('Exception: Function only accepts integer value')
    return ', '.join([str(x) for x in range(n + 1)
                      if x % 5 == 0 and x % 7 == 0])


print(question68_divis_5_7(100))
