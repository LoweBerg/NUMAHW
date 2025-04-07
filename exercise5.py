from scipy.integrate import quad
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt


# Task 1
def p(x, a=1, b=0, c=0, d=0):
    return a*x**3 + b*x**2 + c*x + d


# Task 2
# Vi antar här att coef ges på formen a, b, c, d
def p2(x, *coef):
    return coef[0]*x**3 + coef[1]*x**2 + coef[2]*x + coef[3]


# Task 4
# Vi antar här att coef ges på formen a, b, c, d, ...
def p3(x, *coef):
    s = 0
    for i in range(len(coef)):
        s += coef[i]*x**(len(coef)-1-i)
    return s


# Task 5
def sin(x, omega):
    return np.sin(omega * x)


print(quad(sin, 0, np.pi/2, 2*np.pi))

# Task 6
coefs = np.linspace(0, 2*np.pi, 1000)
integrals = [quad(sin, 0, np.pi/2, c)[0] for c in coefs]

plt.figure("Task 6")
plt.suptitle("Integral vs omega")
plt.plot(coefs, integrals)
plt.xlabel("Omega")
plt.ylabel("Integral from 0 to pi/2")
plt.grid()

# Task 7
# Vi gissar att x=10 ligger till höger om den positiva roten
root = fsolve(p3, np.array([10]), (1, 1, -3))
print(root)

# Task 8
# Vi gissar att x=10 alltid ligger till höger om den positiva roten
a_array = np.linspace(1, 5, 100)
roots = [fsolve(p3, np.array([10]), (a, 1, -3)) for a in a_array]

plt.figure("Task 8")
plt.suptitle("Positive root coordinate vs a")
plt.plot(a_array, roots)
plt.xlabel("a")
plt.ylabel("Location of positive root")
plt.grid()

plt.show()
