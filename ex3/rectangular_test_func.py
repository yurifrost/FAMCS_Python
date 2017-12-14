#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Python 3.5.3
"""
Ручные вычисления:
    1 * f(1.5) + 1 * f(2.5) = 6.75 + 31.25 = 38
"""
manual_calc = 38


def rectangular(f, a, b, n):
    h = float(b - a)/n
    result = f(a + 0.5 * h)
    for i in range(1, n):
        result += f(a + 0.5 * h + i * h)
        result *= h
        return result


def test_func():

    res = rectangular(lambda x: 2 * (x ** 3), 1, 3, 2)
    print('Результат функции: {}'.format(res))
    print('Совпадают ли вычисления: {}'.format(res == manual_calc))


test_func()
