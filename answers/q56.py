#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Question56Error(Exception):
    __slots__ = ('_message')

    def __init__(self, message):
        self._message = message


try:
    raise Question56Error('Question56')
except Question56Error as message:
    print(message)
