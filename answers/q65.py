#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question65_fibonacci(n):
    if not isinstance(n, int):
        raise ValueError('Exception: Function only accepts integer value')
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return question65_fibonacci(n - 1) + question65_fibonacci(n - 2)


def question65_fibonacci_tail_recursion(n, result=1):
    if not isinstance(n, int):
        raise ValueError('Exception: Function only accepts integer value')
    if n == 1:
        return result
    else:
        return question65_fibonacci_tail_recursion(n - 2, result + n - 1)


def question65_fibonacci_generator(n):
    if not isinstance(n, int):
        raise ValueError('Exception: Function only accepts integer values')
    i, a, b = 0, 0, 1
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


print(question65_fibonacci(10))
print(question65_fibonacci_tail_recursion(5))
print(list(question65_fibonacci_generator(8))[-1:])
print(list(question65_fibonacci_generator(10)))
