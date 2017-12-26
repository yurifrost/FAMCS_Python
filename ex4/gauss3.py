import numpy as np


def build_lu3(A):
    lu = np.array(A, float)
    for k in range(lu.shape[0] - 1):
        lu[k + 1, k] /= lu[k, k]
        lu[k + 1, k + 1] -= lu[k, k + 1] * lu[k + 1, k]
    return lu


def solve_lu3(A, b):
    lu = build_lu3(A)
    b = np.array(b, float)
    for i in range(1, len(b)):
        b[i] -= lu[i, i - 1] * b[i - 1]
    b[len(b) - 1] /= lu[len(b) - 1, len(b) - 1]
    for i in range(len(b) - 2, -1, -1):
        b[i] = (b[i] - lu[i, i + 1] * b[i + 1]) / lu[i, i]
    return b


def test_solve_lu3():
    A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    expected = np.array([2. / 9, 2. / 9, 0])
    b = np.array([2. / 9, 2. / 9, -2. / 9])
    computed = solve_lu3(A, b)
    tol = 1e-14
    success = np.linalg.norm(computed - expected) < tol
    msg = 'x_exact = ' + str(expected) + '; x_computed = ' + str(computed)
    assert success, msg


def test_determinant():
    A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    expected = 4
    lu = build_lu3(A)
    computed = np.linalg.det(np.diag(np.diag(lu)))
    tol = 1e-14
    success = computed - expected < tol
    msg = 'x_exact = ' + str(expected) + '; x_computed = ' + str(computed)
    assert success, msg