#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def question57_name_company(email):
    if not isinstance(email, str):
        raise ValueError('Exception: Function only accepts String value')
    username_programe = re.compile('\w+(?=@\w+\.\w+)')
    company_programe = re.compile('(?<=\w@)\w+(?=\.\w+)')
    username = username_programe.search(email)
    companyname = company_programe.search(email)
    return ('Username: ' + username.group(0) + '\n' + 'Company: '
            + companyname.group(0))


print(question57_name_company('username@companyname.com'))
