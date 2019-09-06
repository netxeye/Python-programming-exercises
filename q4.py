#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def conver_number(s):
    if str(s) and str(s).find(',') != -1:
        return (str(s).split(sep=','), tuple(str(s).split(sep=',')))
    else:
        return 'wrong type of data',


input_data = input('please list of number:')
for d in conver_number(input_data):
    print(d)
