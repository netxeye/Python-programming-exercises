#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from timeit import Timer


def question81Exec100(command, times=101):
    if (
            (not isinstance(command, str))
            or
            (not isinstance(times, int))
       ):
        raise ValueError('''
        Exception: Aritribute command has to be string
                   Artribute times has to be integer
        ''')
    __commands = 'for i in range(' + str(times) + '): ' + command
    print(__commands)
    return Timer(__commands)


print(question81Exec100('1 + 1').timeit(), 'seconds')
