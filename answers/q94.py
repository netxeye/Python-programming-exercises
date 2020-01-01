#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question94CountCharaters(s):
    if not isinstance(s, str):
        raise ValueError('Exception: Function only accepts string value')
    for x in s:
        print(x + ',', s.count(x))


def question94CountCharaters2(s):
    if not isinstance(s, str):
        raise ValueError('Exception: Function only accepts string value')
    dic = dict()
    for x in s:
        dic[x] = dic.get(x, 0) + 1
    return dic


print(question94CountCharaters('abcdefgabc'))
for k, v in question94CountCharaters2('abcdefgabc').items():
    print(k + ',', v)
