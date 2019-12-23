#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class American(object):
    __slots__ = ('_national')

    def __init__(self, national='CA'):
        self._national = national

    def __doc__(self):
        return '''
        This is Question 49
        '''

    @property
    def national(self):
        return self._national

    @national.setter
    def national(self, national):
        if not isinstance(national, str):
            raise ValueError('Exception: national only accepts string value')
        self._national = national

    def printNationality(self):
        print(self._national)


persone1 = American()
persone2 = American()
persone3 = American()
persone1.national = 'WA'
persone3.national = 'CHINA'
persone1.printNationality()
persone2.printNationality()
persone3.printNationality()
print(persone3.national)
