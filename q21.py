#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt


def question21_distance(step_dict):
    horizon, vertical = 0, 0
    for key, value in step_dict.items():
        if key.lower() == 'up':
            vertical += value
        elif key.lower() == 'down':
            vertical -= value
        elif key.lower() == 'left':
            horizon -= value
        elif key.lower() == 'right':
            horizon += value
        else:
            raise ValueError('Direction only accept: "UP", "Down", "Left"' +
                             ', "Right"')
    return sqrt(horizon ** 2 + vertical ** 2)
