#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question63_compute(int_input):
    if not isinstance(int_input, (int, float)):
        raise ValueError('Exception: Function only accepts interger or float')
    if int_input == 1:
        return 1 / 2
    else:
        return int_input / (int_input + 1) + question63_compute(int_input - 1)


def question63_iter(n, product=0.5):
    if not isinstance(n, (int, float)):
        raise ValueError('Exception: Function only accepts interger or float')
    if n == 1:
        return product
    else:
        return question63_iter(n - 1, product + n / (n + 1))


print(question63_compute(500))
print(question63_iter(500))
