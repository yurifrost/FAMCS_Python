from numpy import zeros, log


def rectangular(f, a, b, n, rec='left'):
    if rec == 'left':
        get_node = lambda i: i
    elif rec == 'right':
        get_node = lambda i: i + 1
    elif rec == 'mid':
        get_node = lambda i: i + 0.5
    else:
        return float('nan')

    h = float(b - a) / n
    result = 0

    for i in range(0, n):
        result += f(a + get_node(i) * h)
    result *= h

    return result


def test_rectangular_manual():
    rec = ['left', 'mid', 'right']
    expected = [184, 376, 688]
    f = lambda x: x ** 2 + x ** 3
    for i in range(len(rec)):
        computed = rectangular(f, 0, 6, 3, rec[i])
        tol = 1E-14
        rel_error = abs(expected[i] - computed)
        msg = "Погрешность {0} больше допуска {1}.".format(rel_error, tol)
        assert rel_error < tol, msg


def test_rectangular_constant():
    v = lambda x: 10
    V = lambda x: 10 * x
    a = 1
    b = 5
    expected = V(b) - V(a)
    rec = ['left', 'mid', 'right']
    for i in range(len(rec)):
        computed = rectangular(v, a, b, 2, rec[i])
        tol = 1E-15
        rel_error = abs(expected - computed)
        msg = "Погрешность: {0}".format(rel_error)
        assert rel_error < tol, msg


def conv_rates(f, F, a, b, rec, num_exp = 14):
    expected = F(b) - F(a)
    n = zeros(num_exp, dtype=int)
    E = zeros(num_exp)
    r = zeros(num_exp)
    for i in range(num_exp):
        n[i] = 2 ** (i + 1)
        computed = rectangular(f, a, b, n[i], rec)
        E[i] = abs((expected - computed) / expected)
        if i > 0:
            r_im1 = log(E[i] / E[i-1]) / log(float(n[i] / n[i - 1]))
            r[i - 1] = float('%.2f' % r_im1)
    return r


def test_rectangular_conv_rates():
    v = lambda x: x
    V = lambda x: x ** 2 / 2.
    a = 0; b = 4
    rec = ['left', 'right', 'mid']
    for i in range(len(rec)):
        r = conv_rates(v, V, a, b, rec[i])
        tol = 0.01
        msg = str(r[-4:])
        success = (abs(r[-1]) - 2) < tol
        assert success, msg