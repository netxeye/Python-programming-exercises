#! /usr/bin/evn python3
# -*- coding: utf-8 -*-


def questin32_print_key(dictionary):
    if (1 in dictionary.keys()) or (2 in dictionary.keys()) or (3 in dictionary.keys()):
        raise ValueError('Exception: The dictionary has to contain 1, 2 or 3')

