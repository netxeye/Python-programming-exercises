#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question61_decode(string_value):
    if not isinstance(string_value, bytes):
        raise ValueError('Exception: Function only accepts bytes Value')
    return string_value.decode('utf-8')


print(question61_decode('hello world'.encode('ascii')))
