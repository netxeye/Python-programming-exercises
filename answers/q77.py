#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import sample


def question77RandomEven(start, end):
    if (
        (not isinstance(start, int))
        or
        (not isinstance(end, int))
       ):
        raise ValueError('Ecxception: Function only accepts integer value')
    return sample([x for x in range(start, end)
                   if x % 2 != 0
                   ], 5)


print(question77RandomEven(100, 201))
