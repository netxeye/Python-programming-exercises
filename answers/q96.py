#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question96Indexes(s):
    if not isinstance(s, str):
        raise ValueError('Exception: Function only accepts String')
    characters = s[::2]
    indexes = s[1::2]
    lis = list(range(len(characters) - 1))
    for x in indexes:
        lis[int(x) - 1] = characters[int(x) - 1]
    return ''.join(lis) + characters[-1:]


print(question96Indexes('H1e2l3l4o5w6o7r8l9d'))
