#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class American(object):
    pass


class NewYorker(American):
    pass


american1 = American()
newyorker1 = NewYorker()
print(american1)
print(newyorker1)
print(isinstance(newyorker1, American))
print(isinstance(american1, NewYorker))
