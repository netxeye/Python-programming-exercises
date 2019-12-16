#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def pow2_dic(end):
    number_range = tuple(map(str, range(0, 10)))
    if end and str(end) in number_range:
        return dict(zip(list(range(1, int(end) + 1)), list(
            map(lambda x: x ** 2, range(1, int(end) + 1)))))
    else:
        return {}


print(pow2_dic(8))
print(pow2_dic('8'))
print(pow2_dic('www'))
