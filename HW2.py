import numpy as np
import matplotlib.pyplot as plt


# Task 1
class Interval:
    def __init__(self, left, right=None):
        self._left = left
        # Task 7
        if right is None:
            self._right = left
        else:
            self._right = right

    # Task 2
    def __add__(self, other):
        if isinstance(other, int):
            return Interval(self._left + other, self._right + other)
        if isinstance(other, float):
            return Interval(float(self._left) + other, float(self._right) + other)
        if isinstance(other, Interval):
            return Interval(self._left + other._left, self._right + other._right)
        raise TypeError("Operands must both be intervals!")

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            return Interval(self._left - other, self._right - other)
        if isinstance(other, float):
            return Interval(float(self._left) - other, float(self._right) - other)
        if isinstance(other, Interval):
            return Interval(self._left - other._right, self._right - other._left)
        raise TypeError("Operands must both be intervals!")

    def __rsub__(self, other):
        return Interval(other) - self

    def __mul__(self, other):
        if isinstance(other, int):
            return Interval(self._left * other, self._right * other)
        if isinstance(other, float):
            return Interval(float(self._left) * other, float(self._right) * other)
        if isinstance(other, Interval):
            return Interval(min(self._left * other._left,
                                self._left * other._right,
                                self._right * other._left,
                                self._right * other._right)
                            ,
                            max(self._left * other._left,
                                self._left * other._right,
                                self._right * other._left,
                                self._right * other._right))
        raise TypeError("Operands must both be intervals!")

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Operands must both be intervals!")
        # Task 6
        if 0 in other:
            raise ValueError("Numerator must not contain zero!")
        return Interval(min(self._left / other._left,
                            self._left / other._right,
                            self._right / other._left,
                            self._right / other._right)
                        ,
                        max(self._left / other._left,
                            self._left / other._right,
                            self._right / other._left,
                            self._right / other._right))

    def __rtruediv__(self, other):
        return other / self

    def __neg__(self):
        return Interval(-self._left, -self._right)

    # Task 9
    def __pow__(self, other):
        if not isinstance(other, int):
            raise TypeError("Exponent must be an integer!")
        if not other > 0:
            raise ValueError("Exponent must be strictly positive!")

        if other % 2:
            return Interval(self._left**other, self._right**other)

        if self._left >= 0:
            return Interval(self._left ** other, self._right ** other)
        if self._right < 0:
            return Interval(self._right ** other, self._left ** other)
        return Interval(0, max(self._left ** other, self._right ** other))

    # Task 3
    def __repr__(self):
        return f'[{self._left}, {self._right}]'

    # Task 5
    def __contains__(self, item):
        return self._left <= item <= self._right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, val):
        self._left = val

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, val):
        self._right = val


if __name__ == '__main__':
    i = Interval(1, 2)
    print(i)
    print("-"*30)
    I1 = Interval(1, 4)  # [1 , 4 ]
    print(I1)
    I2 = Interval(-2, - 1)  # [ -2 , -1 ]
    print(I2)
    print(I1 + I2)  # [ -1 , 3 ]
    print(I1 - I2)  # [2 , 6 ]
    print(I1 * I2)  # [ -8 , -1 ]
    print(I1 / I2)  # [ - 4 . , - 0 . 5 ]
    print("-"*30)
    # Task 8
    print(Interval(2, 3) + 1)  # [3 , 4 ]
    print(1 + Interval(2, 3))  # [3 , 4 ]
    print(1.0 + Interval(2, 3))  # [ 3 .0 , 4 . 0 ]
    print(Interval(2, 3) + 1.0)  # [ 3 .0 , 4 . 0 ]
    print(1 - Interval(2, 3))  # [ -2 , -1 ]
    print(Interval(2, 3) - 1)  # [1 , 2 ]
    print(1.0 - Interval(2, 3))  # [ - 2 .0 , -1 . 0 ]
    print(Interval(2, 3) - 1.0)  # [ 1 .0 , 2 . 0 ]
    print(Interval(2, 3) * 1)  # [2 , 3 ]
    print(1 * Interval(2, 3))  # [2 , 3 ]
    print(1.0 * Interval(2, 3))  # [ 2 .0 , 3 . 0 ]
    print(Interval(2, 3) * 1.0)  # [ 2 .0 , 3 . 0 ]
    print(- Interval(4, 5))  # [-4, -5]
    print("-" * 30)
    x = Interval(-2, 2)  # [ -2 , 2 ]
    print(x**2)  # [ 0 , 4 ]
    print(x**3)  # [ -8 , 8 ]
    print("-" * 30)
    # Task 10
    xl = np.linspace(0., 1, 1000)
    xu = np.linspace(0., 1, 1000) + 0.5
    intervals = [Interval(0)] * 1000
    for i in range(np.size(xl)):
        intervals[i] = Interval(xl[i], xu[i])

    polynomial = [3*(X**3) - 2*(X**2) - 5*X - 1 for X in intervals]
    yl = [X.left for X in polynomial]
    yu = [X.right for X in polynomial]

    plt.plot(xl, yl, color="blue")
    plt.plot(xl, yu, color="green")
    plt.title(r"$p(I) = 3I^3 − 2I^2 − 5I − 1$, I = Interval(x, x + 0.5)")
    plt.xlabel("x")
    plt.ylabel("p(I)")
    plt.xlim(0.0, 1.0)
    plt.ylim(-10, 4)
    plt.show()
