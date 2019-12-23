#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question44_even_list(data_list):
    if not isinstance(data_list, list):
        raise ValueError('Exception: Function only accpets list value')
    return [x for x in data_list if x % 2 == 0]


def question44_filter(data_list):
    if not isinstance(data_list, list):
        raise ValueError('Exception: Function only accepts list value')
    return list(filter(lambda x: x % 2 == 0, data_list))


print(question44_even_list(list(range(1, 11))))
print(question44_filter(list(range(1, 11))))
