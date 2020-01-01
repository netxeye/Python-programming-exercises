#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question91Zip(lis1, lis2):
    if (
            (not isinstance(lis1, list))
            or
            (not isinstance(lis2, list))
       ):
        raise ValueError('Exception: Function only accepts list value')
    return zip(lis1, lis2)


def question91IAnd(lis1, lis2):
    if (
            (not isinstance(lis1, list))
            or
            (not isinstance(lis2, list))
       ):
        raise ValueError('Exception: Function only accepts list value')
    set1 = set(lis1)
    set2 = set(lis2)
    set1 &= set2
    return list(set1)


print(question91IAnd([1, 3, 6, 78, 35, 55], [12, 24, 35, 24, 88, 120, 155]))
print(list(question91Zip([1, 3, 6, 78, 35, 55],
      [12, 24, 35, 24, 88, 120, 155])))
