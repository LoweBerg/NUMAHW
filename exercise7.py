import numpy as np
import matplotlib.pyplot as plt


# Task 1
def eigenvector_test(input_matrix: np.ndarray):
    if input_matrix.shape[0] != input_matrix.shape[1]:
        print()
        raise ValueError(f"Input array must be square! Dimensions were {input_matrix.shape}")
    if not np.array_equal(input_matrix, np.matrix_transpose(input_matrix)):
        raise ValueError("Input array must be symmetrical!")

    eigenvalues, eigenvectors = np.linalg.eig(input_matrix)

    inv_eigenvectors = np.matrix_transpose(eigenvectors)
    unit_matrix = np.eye(eigenvectors.shape[0])
    diagonal_matrix = eigenvectors @ inv_eigenvectors
    # We return True if
    return np.allclose(diagonal_matrix, np.diag(np.diag(diagonal_matrix)))


A = np.array([
            [1, 2, 3, 4, 5],
            [2, 1, 2, 3, 4],
            [3, 2, 1, 2, 3],
            [4, 3, 2, 1, 2],
            [5, 4, 3, 2, 1]
            ])

B = np.array([
            [3, -2, 11, 4, -5],
            [-2, 3, -2, 11, 4],
            [11, -2, 3, -2, 11],
            [4, 11, -2, 3, -2],
            [-5, 4, 11, -2, 3]
            ])

print(eigenvector_test(A))
print(eigenvector_test(B))

print("-"*20)


# Task 2
def bad_construct_matrix(v: np.ndarray) -> np.ndarray:
    size = v.shape[0]
    result = np.zeros((size, size))
    for i in range(size):
        result[i, i] = v[i] * -2
    for i in range(size-1):
        result[i+1, i] = v[i]
    for i in range(size-1):
        result[i, i+1] = v[i+1]

    return result


def construct_matrix(v: np.ndarray) -> np.ndarray:
    size = v.shape[0]
    result = np.zeros((size, size))
    result += np.diag(v * -2)
    result += np.diag(v[1:], 1)
    result += np.diag(v[:-1], -1)

    return result


v = np.array([1, 2, 3])
print(bad_construct_matrix(v))
print(construct_matrix(v))

print("-"*20)

# Task 3
u = np.linspace(0, 2*np.pi, 500)
D = construct_matrix(u)
sinD = np.sin(D)
one_vector = np.full(D.shape[0], 1.0)
y = one_vector @ D
plt.plot(u, y)
plt.show()
