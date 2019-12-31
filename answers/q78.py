#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import sample


def question78Random(start, end):
    if (
            (not isinstance(start, int))
            or
            (not isinstance(end, int))
       ):
        raise ValueError('Exception: Function only accepts integer value')
    return sample(
            [x for x in range(start, end)
                if x % 5 == 0 and x % 7 == 0
             ], 5)


print(question78Random(1, 1001))
