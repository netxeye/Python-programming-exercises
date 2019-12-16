#! /bin/env python3
# -*- coding: utf-8 -*-

class QuestionClass:
    def getString(self):
        try:
            input_line = input('Enter String: ')
            self.input_line = input_line
        except TypeError as TE:
            print('Worng formate', TE)

    def printString(self):
        print('Printing the string in upper case', self.input_line.upper())


a = QuestionClass()
a.getString()
b = QuestionClass()
b.getString()
a.printString()
b.printString()
