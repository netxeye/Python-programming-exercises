#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question95Reverse(s):
    if not isinstance(s, str):
        raise ValueError('Ecxception: Function only accepts String value')
    return ''.join(reversed(s))


def question95Reverse2(s):
    if not isinstance(s, str):
        raise ValueError('Ecxception: Function only accepts String value')
    return s[::-1]


print(question95Reverse('abcdefgabc'))
print(question95Reverse2('abcdefgabc'))
