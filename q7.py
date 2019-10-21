#! /bin/env python3
# -*- coding: utf-8 -*-

def two_dimension_array(x,y):
    two_dimension = [[0 for y_value in range(y)] for x_value in range(x)]
    for x_value in range(x):
        for y_value in range(y):
            two_dimension[x_value][y_value] = x_value * y_value
    return two_dimension

print(two_dimension_array(3,5))

def two_dimension_array_2(x,y):
    return [[x_value * y_value for y_value in range(y)] for x_value in range(x)]

print(two_dimension_array_2(3,5))
