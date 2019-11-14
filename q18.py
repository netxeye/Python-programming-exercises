#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import string


class Question18Password(object):
    '''
    Password Checking:
    '''
    __slots__ = ('_password')

    def __init__(self, password='Welcome@20'):
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        _vailable_upper = False
        _vailable_lower = False
        _vailable_number = False
        _vailable_chacter = False
        if not isinstance(value, str):
            raise ValueError('Password only accept str')
        for upper_case in string.ascii_uppercase:
            if upper_case in value:
                _vailable_upper = True
                break
        for lower_case in string.ascii_lowercase:
            if lower_case in value:
                _vailable_lower = True
                break
        for number in string.digits:
            if number in value:
                _vailable_number = True
                break
        for chacter in '$#@':
            if chacter in value:
                _vailable_chacter = True
                break
        if not _vailable_upper:
            raise ValueError('Password should contain at least 1 upper letter')
        if not _vailable_lower:
            raise ValueError('Password should contain at least 1 lower letter')
        if not _vailable_number:
            raise ValueError('Password should contain at least 1 number')
        if not _vailable_chacter:
            raise ValueError(r'Password should contain at least 1 from' +
                             ' "$" "#" "@"')
        if len(value) < 6:
            raise ValueError('Minimum length of password should be 6')
        if len(value) > 12:
            raise ValueError('Manimum length of password should be 12')
        self._password = value


new_password1 = Question18Password()
new_password2 = Question18Password()
print(new_password1.password)
try:
    password_input = input('Eneter your Password: ')
    new_password2.password = password_input
except ValueError as error_message:
    print('Error:', error_message)
print(new_password2.password)
