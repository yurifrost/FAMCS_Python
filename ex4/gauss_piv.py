import numpy as np


def gauss(x):
    x = np.array(x, float)
    return x[1:] / x[0]


def gauss_app(C, t):
    C = np.array(C, float)
    t = np.array([[t[i]] for i in range(len(t))], float)
    C[1:, :] = C[1:, :] - t * C[0, :]
    return C


def build_lu_piv(A):
    lu = np.array(A, float)
    piv = np.array(range(lu.shape[0]))
    for k in range(lu.shape[0]):
        mu = k + np.argmax(A[k:, k])
        lu[[k, mu], :] = lu[[mu, k], :]
        piv[[k, mu]] = piv[[mu, k]]
        if lu[k, k] != 0:
            t = gauss(lu[k:, k])
            lu[k + 1:, k] = t
            lu[k:, k + 1:] = gauss_app(lu[k:, k + 1:], t)
    return lu, piv


def solve_lu_piv(A, b):
    lu, piv = build_lu_piv(A)
    b = np.array([b[i] for i in piv], float)
    for i in range(1, len(b)):
        b[i] = b[i] - np.dot(lu[i, :i], b[:i])
    for i in range(len(b) - 1, -1, -1):
        b[i] = (b[i] - np.dot(lu[i, i + 1:], b[i + 1:])) / lu[i, i]
    return b


def test_solve_lu_piv():
    A = np.array([[3, 17, 10], [2, 4, -2], [6, 18, -12]])
    expected = np.array([3, 2, 1])
    b = np.dot(A, expected)
    computed = solve_lu_piv(A, b)
    tol = 1e-14
    success = np.linalg.norm(computed - expected) < tol
    msg = 'x_exact = ' + str(expected) + '; x_computed = ' + str(computed)
    assert success, msg