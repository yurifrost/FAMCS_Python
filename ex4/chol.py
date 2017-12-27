import numpy as np


def build_hilbert_matrix(n):
    A = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            A[i, j] = 1 / (i + j + 1)

    return A


def cholesky_decomposition(A):
    n = A.shape[0]
    G = np.zeros((n, n))

    for i in range(n):
        for j in range(i):
            G[i, j] = (A[i, j] - sum(G[i, :j] * G[j, :j])) / G[j, j]

        G[i, i] = (A[i, i] - sum(G[i, :i] ** 2)) ** 0.5

    return G


def cholesky_determinant(G):
    return np.product(G[np.diag_indices(len(G))] ** 2)


n = 4
A = build_hilbert_matrix(n)
G = cholesky_decomposition(A)

print('G:')
print(G)
print('Determinant of a Cholesky matrix: ', cholesky_determinant(G))