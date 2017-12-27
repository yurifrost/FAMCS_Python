import numpy as np
import matplotlib.pyplot as plt


def build_matrix(n, alpha):
    return np.eye(n) * alpha + \
        np.eye(n, k=1) * (-1 - alpha) + \
        np.eye(n, k=-1) * (-1 + alpha)


def build_vector(n, alpha):
    result = np.zeros(n)
    result[0] = 1 - alpha
    result[n - 1] = 1 + alpha
    return result


def sor(A, b, w, eps):
    A = np.array(A, float)
    x = np.array(b, float)
    iter_amount = 0
    while True:
        for i in range(x.shape[0]):
            x[i] = w * (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(
                A[i, i + 1:], x[i + 1:])) / A[i, i] + (1 - w) * x[i]
        iter_amount += 1
        if np.linalg.norm(np.dot(A, x) - b) < eps or iter_amount > 200:
            break
    return x, iter_amount


def test_sor():
    n = 5
    alpha = 0.2
    A = build_matrix(n, alpha)
    expected = np.array([3, 2, 1, 4, 5])
    b = np.dot(A.T, np.dot(A, expected))
    A = np.dot(A.T, A)
    tol = 1e-5
    computed, iter_amount = sor(A, b, 1.65, tol)
    print('Iterations: ' + str(iter_amount))
    success = np.linalg.norm(computed - expected) < tol
    msg = 'x_exact = ' + str(expected) + '; x_computed = ' + str(computed)
    assert success, msg


def draw(n, alpha):
    b = build_vector(n, alpha)
    A = build_matrix(n, alpha)
    b = np.dot(A.T, b)
    A = np.dot(A.T, A)
    eps = 1e-5
    m = 100
    w_vector = np.linspace(0, 2, m)
    iter_vector = np.zeros(m)
    for i in range(m):
        _, iter_vector[i] = sor(A, b, w_vector[i], eps)
    plt.plot(w_vector, iter_vector)
    plt.xlabel('w')
    plt.ylabel('iterations')
    plt.show()

draw(5, 0.2)