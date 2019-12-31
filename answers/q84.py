#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import sample


def question84Sample(s, v, o):
    if (
            (not isinstance(s, list))
            or
            (not isinstance(v, list))
            or
            (not isinstance(o, list))
       ):
        raise ValueError('Exception: Functon only accepts list value')
    __subject = sample(s, 1)
    __verb = sample(v, 1)
    __object = sample(o, 1)
    return __subject + __verb + __object


print(question84Sample(['I', 'You'], ['Play', 'Love'], ['Hockey', 'Football']))
