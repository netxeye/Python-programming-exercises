#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question69_assert(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    for item in lis:
        assert item % 2 == 0, 'Exception: The list is not an even list'
    return True


try:
    print(repr(question69_assert([2, 4, 6, 8])))
    print(repr(question69_assert([3, 5, 7, 9])))
except AssertionError as message:
    print(message)
