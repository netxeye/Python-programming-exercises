#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def question58_company(email):
    if not isinstance(email, str):
        raise ValueError('Exception: Function only accepts String Value')
    company_programe = re.compile('(?<=\w@)\w+(?=\.\w+)')
    return company_programe.search(email).group(0)


print(question58_company('Mike@perfectworld.com'))
