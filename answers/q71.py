#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question71_search(arr, l, r, x):
    if not isinstance(arr, list):
        raise ValueError('Exception: Parameter arr only accepts list value')
    if not isinstance(l, int):
        raise ValueError('Exception: Parameter l only accepts integer value')
    if not isinstance(r, int):
        raise ValueError('Exception: Parameter r only accepts integer value')
    if r >= l:
        mid = int(l + (r - l)/2)
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return question71_search(arr, l, mid-1, x)
        else:
            return question71_search(arr, mid+1, r, x)
    else:
        return -1


arr = list(range(1000))
x = 73
print(question71_search(arr, 0, len(arr)-1, x))
