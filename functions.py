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

