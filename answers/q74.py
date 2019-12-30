#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random


def question74Random(start, end):
    if ((not isinstance(start, (int, float)))
        or
       (not isinstance(end, (int, float)))):
        raise ValueError('Exception: Function only accepts integer or float')
    return random.choice([x for x in range(start, end) if x % 2 == 0])


print(question74Random(1, 1100))
