#! /usr/bin/env python3
# -*- coding: utf-8 -*-
input_data = input('Please Enter a string, we will count the words: ')
input_list = input_data.split(' ')
input_list.sort()
input_dic = {}
for word in input_list:
    input_dic[word] = input_data.count(word)
for word in input_dic.keys():
    print(word + ':', input_dic[word])
