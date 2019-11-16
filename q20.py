#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time


def question20_devisable_by_7(end, start=0):
    '''
    This function generator which uses for create iterate numbers,
    which are divisiable.
    paramater:
    start default value is 0
    end the end of range, not included
    '''
    item = start
    while item < end:
        if item % 7 == 0:
            yield item
        item += 1


def question20_devisable_by_7_1(end, start=0):
    '''
    Testing while and range, I guess range would be faster than while loop
    '''
    for item in range(start, end):
        if item % 7 == 0:
            yield item


def question20_devisable_by_7_generator(end, start=0):
    '''
    () could create gernerator. the way is same as
    list comperhensions
    looks like this way would be more effeiction
    '''
    return (i for i in range(start, end) if i % 7 == 0)


for i in range(20):
    print('the fist way by while')
    start_time = time()
    print(question20_devisable_by_7(1000))
    print('---- %s seconds ----' % (time() - start_time))
    print('the second way by () genterator')
    start_time = time()
    print(question20_devisable_by_7_generator(1000))
    print('---- %s seconds ----' % (time() - start_time))
    print('the third way, by using range and for')
    start_time = time()
    print(question20_devisable_by_7_1(1000))
    print('---- %s seconds ----' % (time() - start_time))
