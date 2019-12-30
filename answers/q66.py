#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question66_fibonacci_generator(n):
    if not isinstance(n, int):
        raise ValueError('Exception: Function only accepts int value')
    i, a, b = 0, 0, 1
    while i <= n:
        yield a
        a, b = b, a + b
        i += 1


print(list(question66_fibonacci_generator(70)))
