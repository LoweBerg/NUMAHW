import numpy as np


def approx_ln(x: float, n: int) -> float:
    """"
    Gives an approximation of ln(x) for some x > 0 after n iterations
    """
    if x <= 0:
        raise ValueError('x argument must be greater than zero!')

    a: float = (x + 1) / 2
    g: float = np.sqrt(x)
    for i in range(n):
        a = (a+g)/2
        g = np.sqrt(a*g)

    return (x - 1) / a


def fast_approx_ln(x: float, n: int) -> float:
    """"
    Gives an approximation of ln(x) for some x > 0 after n iterations using an auxiliary array to
    speed up convergence
    """
    if x <= 0:
        raise ValueError('x argument must be greater than zero!')

    a: float = (x + 1) / 2
    g: float = np.sqrt(x)
    d: np.ndarray = np.zeros((n+1, n+1))
    for i in range(n+1):
        d[0][i] = a
        a = (a+g)/2
        g = np.sqrt(a*g)

    for k in range(1, n+1):
        for i in range(k, n+1):
            d[k][i] = (d[k-1][i]-(4**-k)*d[k-1][i-1])/(1-4**-k)

    return (x - 1) / d[n][n]
