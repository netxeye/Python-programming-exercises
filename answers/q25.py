#! /usr/bin/evn python3
# -*- coding: utf-8 -*-


class Question25(object):
    'Question class for practices'

    __slots__ = ('_msg', '_testing')
    def __init__(self, msg):
        self._msg = msg
        self._testing = 0

    def __doc__():
        '''
        This is class qusetion25' doc
        '''

    def get_message(self):
        print(self._msg)

    @property
    def testing(self):
        return self._testing

    @testing.setter
    def testing(self, value):
        if not isinstance(value, int):
            raise ValueError('porperty1 must be integer')
        self._testing = value

new_ob1 = Question25('testing')
new_ob1.get_message()
print(new_ob1.__doc__)
print(new_ob1.testing)
try:
    new_ob1.testing = 'testing'
except ValueError as message:
    print(message)
new_ob1.testing = 20
print(new_ob1.testing)
