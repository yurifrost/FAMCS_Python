#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 3.5.3


def trapezoidal(f, a, b, n):
	"""
	Вычисляет приближенное значение интеграла с помощью формулы трапеций
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
	h = float(b - a)/n
	result = 0.5*(f(a) + f(b))
	for i in range(1, n):
		result += f(a + i*h)
	result *= h
	return result


def test_trapezoidal_one_exat_value_2():
	"""
	Тестирование на результатах, полученных в ручную
	"""
	from math import exp
	v = lambda x: x ** 0.5
	n = 2
	expected = 2 + 2 * (2 ** 0.5)
	computed = trapezoidal(v, 0, 4, n)
	rel_error = abs(expected - computed)
	tol = 1E-15
	success = rel_error < tol
	msg = 'погрешность = %.17f больше допуска = %.17f' % (rel_error, tol)
	assert success, msg


def test_trapezoidal_one_exat_value_3():
	"""
	Тестирование на результатах, полученных в ручную
	"""
	from math import exp
	v = lambda x: x ** 0.5
	n = 3
	expected = (8 * (3 ** 0.5) * (1 + (2 ** 0.5)) + 12) / 9.0
	computed = trapezoidal(v, 0, 4, n)
	rel_error = abs(expected - computed)
	tol = 1E-15
	success = rel_error < tol
	msg = 'погрешность = %.17f больше допуска = %.17f' % (rel_error, tol)
	assert success, msg


def convergence_rates(f, F, a, b, num_exp = 14):
	"""
	Вычисляются порядки точности для последовательных экспериментов
	Входные параметры:
	f --- подынтегральная функция
	F --- первообразная
	a, b --- пределы интегрирования
	num_exp --- количество последовательных эксперимнетов

	Возвращает массив r со значениями порядков точности
	"""
	from math import log
	from numpy import zeros
	expected = F(b) - F(a)
	n = zeros(num_exp, dtype=int)
	E = zeros(num_exp)
	r = zeros(num_exp - 1)
	for i in range(num_exp):
		n[i] = 2**(i+1)
		computed = trapezoidal(f, a, b, n[i])
		E[i] = abs((expected - computed) / expected)
		if i > 0:
			r_im1 = log(E[i]/E[i-1])/log(float(n[i]/n[i-1]))
			r[i-1] = float('%.2f' % r_im1) # оставляем только два знака после запятой
	return r


def test_trapezoidal_conv_rate():
	"""
	Сравниваем вычисленные порядки точности с ожидаемым -2.
	"""
	from math import exp
	v = lambda x: x ** 0.5
	V = lambda x: (x ** 1.5) * (2.0 / 3)
	a = 0
	b = 4
	r = convergence_rates(v, V, a, b)
	print(r)
	tol = 0.01
	msg = str(r[-4:]) # выводим 4 последних значения массива
	success = (abs(r[-1]) - 2) < tol # сравниваем последнее значение массива
	assert success, msg