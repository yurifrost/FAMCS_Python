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
    return result


def integrate_x2x():
    f = lambda x: x ** x
    a = 0
    b = 4
    eps = 1E-4
    return adaptive_integration(f, a, b, eps)


print(integrate_x2x())