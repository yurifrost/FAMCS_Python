def trapezoidal(f, a, b, n):
	h = float(b - a)/n
	result = 0.5*(f(a) + f(b))
	for i in range(1, n):
		result += f(a + i*h)
	result *= h
	return result


def adaptive_integration(f, a, b, eps, method='trapezoidal'):
    n = 1
    while abs(trapezoidal(f, a, b, n) - trapezoidal(f, a, b, 2 * n)) >= eps:
        n *= 2
    result = trapezoidal(f, a, b, 2 * n)
    print("Погрешность: {0}".format(abs(result - trapezoidal(f, a, b, 2 * n))))
    return result


def test_adaptive_integration():
    v1 = lambda x: x ** 2
    v2 = lambda x: x ** 0.5
    a = 0
    b = 2
    eps1 = 1E-1
    eps2 = 1E-10
    adaptive_integration(v1, a, b, eps1)
    adaptive_integration(v2, a, b, eps2)