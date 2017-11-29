#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Python 3.5.3
"""
Ручные вычисления:

    1 * (f(1) + f(2)) / 2 + 1 * (f(2) + f(3)) / 2 =

  = (2 + 16) / 2 + (16 + 54) / 2 = 9 + 35 = 44
"""
manual_calc = 44


def trapeziodal(f, a, b, n):
    h = float(b - a)/n
    result = 0.5*(f(a) + f(b))
    for i in range(1, n):
        result += f(a + i*h)
        result *= h
        return result


def test_func():
    res = trapeziodal(lambda x: 2 * (x ** 3), 1, 3, 2)
    print('Function result: {}'.format(res))
    print('Do the calculations match: {}'.format(res == manual_calc))

    test_func()