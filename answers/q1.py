#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def find_the_number(start, end):
    ''' start is the postion for start
        end is the postion for end(not included)
    '''
    __L = list()
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            __L.append(i)
    return __L


print('Way1:')
print(find_the_number(2000, 3201))


def find_the_number2(number):
    return number % 7 == 0 and number % 5 != 0


print('Way2:')
print(list(filter(find_the_number2, range(2000, 3201))))
print('Way3:')
print(list(filter(lambda x: x % 7 == 0 and x % 5 != 0, range(2000, 3201))))


def find_the_number3(start, end):
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            yield i


print('Way4:')
print(list(find_the_number3(2000, 3201)))


def find_the_number4(start, end):
    __L = list()

    def apply_filter():
        for i in range(start, end):
            if i % 7 == 0 and i % 5 != 0:
                __L.append(i)
        return __L
    return apply_filter


af = find_the_number4(2000, 3201)
print('Way5:')
print(af())
