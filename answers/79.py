#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randrange


def question79Random(start, end):
    if (
            (not isinstance(start, int))
            or
            (not isinstance(end, int))
       ):
        raise ValueError('Exception: Function only accepts integer value')
    return randrange(start, end)


print(question79Random(7, 16))
