#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question59_search_number(string_input):
    if not isinstance(string_input, str):
        raise ValueError('Exception: Function only accepts String value')
    result = list()
    for item in string_input.split(' '):
        if item in [str(x) for x in range(0, 10)]:
            result.append(item)
    return result


print(question59_search_number('2 cats and 3 dogs'))
