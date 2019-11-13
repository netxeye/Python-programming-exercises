#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Question17Account(object):
    __slots__ = ('_amount')

    def __init__(self, amount=0):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, int):
            raise ValueError('amount must be an integer!')
        else:
            self._amount += value

    def withdrawal(self, value):
        if not isinstance(value, int):
            raise ValueError('withdrawal only accept an integer!')
        else:
            if value < 0:
                raise ValueError('withdrawal can not lower than zero!')
            if value > self._amount:
                raise ValueError('Your account does not have enough money!')
            else:
                self._amount = self._amount - value


account1 = Question17Account()
while True:
    input_date = input(
            'Eneter code and number:(D mean deposit while W means withdrawal)')
    if input_date and ('D' in input_date[0] or 'W' in input_date[0]):
        action = input_date.split(' ')
        if action[0] == 'D':
            account1.amount = int(action[1])
        elif action[0] == 'W':
            account1.withdrawal(int(action[1]))
    else:
        break
print(account1.amount)
account2 = Question17Account(200)
print(account2.amount)
