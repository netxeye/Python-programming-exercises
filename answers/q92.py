#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question92RemoveDuplicated(lis):
    if not isinstance(lis, list):
        raise ValueError('Exception: Function only accepts list value')
    return list(set(lis))


print(question92RemoveDuplicated([12, 24, 35, 24, 88, 120, 15, 88, 120, 155]))
