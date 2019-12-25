#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Rectangle(object):
    __slots__ = ('_length', '_width')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Exception: property length only accepts ' +
                             'integer or float value')
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Exception: property width only accepts ' +
                             'integer or float value')
        self._width = value

    def area(self):
        return self._length * self._width

    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width


newrectangele = Rectangle()
print(newrectangele.length)
print(newrectangele.width)
newrectangele.width = 3.14567
newrectangele.length = 1000
print(newrectangele.area())
try:
    newrectangele.length = 'Testing'
except ValueError as message:
    print(message)
try:
    newrectangele.width = 'Exception'
except ValueError as message:
    print(message)
try:
    newrectangele.notworkingattribute = 'Somthing'
except AttributeError as message:
    print(message)
