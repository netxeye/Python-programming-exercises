#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi


class Circle(object):
    __slots__ = ('_radius', '_pi')

    def __init__(self, radius=20):
        self._radius = radius
        self._pi = pi

    @property
    def radius(self):
        return self._radius

    @property
    def pi(self):
        return self._pi

    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError('Exception: radius only accepts ' +
                             'integer or float values')
        self._radius = radius

    def area(self):
        return self._pi * self.radius ** 2


newcircle = Circle()
print(newcircle.radius)
print(newcircle.pi)
newcircle.radius = 3.133
print(newcircle.radius)
try:
    newcircle.pi = 3.14
except AttributeError as ermessage:
    print(ermessage)
try:
    newcircle.radius = 'Testing'
except ValueError as ermessage:
    print(ermessage)
print(newcircle.pi)
print(newcircle.area())
