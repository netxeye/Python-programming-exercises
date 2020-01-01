#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Person(object):

    def getGender(self):
        pass


class Male(Person):
    __slots__ = ('__gender')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, g):
        if not isinstance(g, str):
            raise ValueError('Exception: Attribute gender has be string value')
        if g.lower() not in ('male'):
            raise ValueError('Exception: Attribute gender has be Male')
        self.__gender = g.title()

    def getGender(self):
        return self.__gender

    def __init__(self):
        self.__gender = 'Male'


class Female(Person):
    __slots__ = ('__gender')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, g):
        if not isinstance(g, str):
            raise ValueError('Exception: Attribute gender has be string value')
        if g.lower() not in ('female'):
            raise ValueError('Exception: Attribute gender has be Female')
        self.__gender = g.title()

    def getGender(self):
        return self.__gender

    def __init__(self):
        self.__gender = 'Female'


aMale = Male()
aFemale = Female()
print (aMale.getGender())
print (aFemale.getGender())
try:
    aMale.gender = 'Test'
except ValueError as message:
    print(message)
