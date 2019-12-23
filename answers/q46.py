#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question46_filter_map(data_list):
    if not isinstance(data_list, list):
        raise ValueError('Exception: Function only accepts list value')
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0,
                data_list)))


print(question46_filter_map(list(range(1, 11))))
