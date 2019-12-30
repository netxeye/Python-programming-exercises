#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import choice


def question75Random(start, end):
    if ((not isinstance(start, int))
       or
       (not isinstance(end, int))):
        raise ValueError('Exception: Function only accepts int')
    return choice([x for x
                   in range(start, end)
                   if x % 5 == 0 and x % 7 == 0])


print(question75Random(1, 100))
