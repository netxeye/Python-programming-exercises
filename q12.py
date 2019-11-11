#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'For my family. Wroking hard is fine'


def question12_even_sequence(start, end):
    'Qeustion 12'
    return [str(number) for number in range(start, end) if number % 2 == 0]


print(','.join(question12_even_sequence(1000, 3001)))
