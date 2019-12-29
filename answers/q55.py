#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question55_error(value=0):
    if not isinstance(value, (int, float)):
        raise ValueError('Exception: Function only accepts integer or float')
    return value / 0


try:
    print(question55_error(33))
except (ValueError, ZeroDivisionError) as message:
    print(message)
except Exception as message:
    print('Catch another error', message)
finally:
    print('Finally')
