#! /usr/bin/evn python3
# -*- coding: utf-8 -*-


def questin32_print_key(init, maximum):
    'Use generater to generate the dict'
    if (not isinstance(int, init)) or (not isinstance(int, maximum)):
        raise ValueError('''
        Exception: thise function only accpets integer value.
        ''')
    return dict((i, i ** 2) for i in range(init, maximum + 1))


print(questin32_print_key(1, 3))
