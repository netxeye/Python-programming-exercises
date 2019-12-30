#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question70_eval(expression):
    if not isinstance(expression, str):
        raise ValueError('Exception: Function only accepts String value')
    return eval(expression)


print(question70_eval('35 + 3'))
