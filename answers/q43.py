#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question43_vaildate_yes(data_str):
    if not isinstance(data_str, str):
        raise ValueError('Exception: Function only accpets String')
    if data_str.lower() == 'yes':
        return 'Yes'
    else:
        return 'No'


print(question43_vaildate_yes('Testing'))
print(question43_vaildate_yes('No'))
print(question43_vaildate_yes('YES'))
