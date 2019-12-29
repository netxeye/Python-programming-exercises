#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Shape(object):

    def area(self):
        return 0


class Square(Shape):
    __slots__ = ('_length')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Exception: property length only accepts' +
                             ' integer or floar')
        self._length = value

    def area(self):
        return self._length ** 2

    def __init__(self, length=0):
        self._length = length


new_square = Square()
print(new_square.area())
new_square.length = 4.75
print(new_square.area())
