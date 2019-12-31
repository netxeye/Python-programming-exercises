#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import sample


def question83Sample(l):
    return sample(l, len(l))


print(question83Sample(list(range(100))))
