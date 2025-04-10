import numpy as np
from numpy.linalg import norm


# Task 3
def matrix_symmetry(array: np.ndarray) -> int:
    if np.array_equal(array, np.transpose(array)):  # Check if symmetric
        return 1
    if np.array_equal(-array, np.transpose(array)):  # Check if skew-symmetric
        return -1
    return 0


A = np.array([[1, 2, 3],
              [2, 4, 7],
              [3, 7, 14]])
print(matrix_symmetry(A))  # Should return 1
B = np.array([[0, 1, 1],
              [-1, 0, 1],
              [-1, -1, 0]])
print(matrix_symmetry(B))  # Should return -1
C = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])
print(matrix_symmetry(C))  # Should return 0
print("-"*20)


# Task 4
def is_orthogonal(x1: np.ndarray, x2: np.ndarray) -> bool:
    """
    Checks if vectors x1 and x2 are orthogonal. Returns True if they are and False otherwise.
    """
    scalar_product = bool(np.dot(x1, x2))  # Boolean is False if np.dot == 0 and True otherwise
    return not scalar_product


v1 = np.array([1, 3, 2])
v2 = np.array([-2, 0, 1])
print(is_orthogonal(v1, v2))  # Should return True
v1 = np.array([2, 4, 2])
v2 = np.array([1, 2, 3])
print(is_orthogonal(v1, v2))  # Should return False
print("-"*20)


# Task 5
def mynormalize(v: np.ndarray) -> np.ndarray:
    length = 0.  # Floating point value is needed
    for e in v:
        length += e**2
    return v / np.sqrt(length)


def npnormalize(v: np.ndarray) -> np.ndarray:
    return v / norm(v)


# Task 6
alpha = np.linspace(0, 2*np.pi, 1000)
result = True
for a in alpha:
    rotation = np.array([[np.cos(a), np.sin(a)],
                         [-np.sin(a), np.cos(a)]])
    A = np.linalg.inv(rotation)
    B = np.transpose(rotation)
    if not np.allclose(A, B):  # The allclose function checks if matrices are equal within a tolerance
        result = False
        break
print(result)  # result will be True if the hypothesis holds for all checked values of alpha
print("-"*20)

# Task 7
A = np.zeros((20, 20))
A += np.diag(np.full(20, 4))
A += np.diag(np.full(19, 1), 1)
A += np.diag(np.full(19, 1), -1)
print(np.linalg.eig(A)[0])
print("-"*20)

# Task 8
A = np.zeros((20, 20))
A += np.diag(np.full(20, 4))
A += np.diag(np.full(19, 1), 1)
A += np.diag(np.full(19, -1), -1)
print(np.linalg.eig(A)[0])

