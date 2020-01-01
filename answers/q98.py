#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def question98Counts(h, l):
    solution = list()
    for c in range(h + 1):
        for r in range(h + 1):
            if 2 * c + 4 * r == l:
                solution.append((c, r))
    return solution


print(question98Counts(35, 94))
