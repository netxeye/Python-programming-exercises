#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question64_compute(n):
    if not isinstance(n, (int, float)):
        raise ValueError('Exception: Function only accepts integer or float')
    if n == 0:
        return 0
    else:
        return question64_compute(n - 1) + 100


def question64_tail_recursion(n, result=0):
    if not isinstance(n, (int, float)):
        raise ValueError('Exception: Function only accepts integer or float')
    if n == 0:
        return result
    else:
        return question64_tail_recursion(n - 1, result + 100)


print(question64_compute(500))
print(question64_tail_recursion(900))
