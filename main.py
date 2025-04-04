from functions import approx_ln, fast_approx_ln
import numpy as np
import matplotlib.pyplot as plt


def main():
    colors = ['blue', 'orange', 'green', 'red', 'purple']

    # Task 2
    x = np.flip(np.linspace(100, 0, 100, False))
    y = np.zeros(np.size(x))
    error = np.zeros(np.size(x))

    fig = plt.figure("Task 2")
    axs = fig.subplots(2)
    fig.suptitle("Task 2")
    for i in range(len(colors)):
        for j in range(np.size(x)):
            y[j] = approx_ln(x[j], i)
            error[j] = abs(np.log(x[j]) - y[j])
        axs[0].plot(x, y, color=colors[i], label=f'approximated logarithm after {i} iterations')
        axs[1].plot(x, error, color=colors[i], label=f'error after {i} iterations')

    axs[0].plot(x, np.log(x), label='numpy natural logarithm')
    axs[0].legend()
    axs[0].set_title("approximated logarithms with different numbers of iterations")
    axs[1].legend()
    axs[1].set_title("error of approximated logarithms")

    # Task 3
    x = 1.41
    n = np.arange(21)
    error = np.zeros(np.size(n))
    for i in range(np.size(n)):
        error[i] = abs(np.log(x) - approx_ln(x, n[i]))

    plt.figure("Task 3")
    plt.xlabel('n')
    plt.ylabel('Error')
    plt.title('Error of approx_ln(1.41, n) for n')
    plt.plot(n, error, color='blue', label=f'|approx_ln(1.41, n) - ln(1.41)|')
    plt.legend()
    plt.grid()

    # Task 4
    x = np.flip(np.linspace(20, 0, 1000, False))
    error = np.zeros(np.size(x))
    plt.figure("Task 4")
    plt.title("Error behavior of the accelerated Carlsson method for the log")
    for i in range(2, 7):
        for j in range(np.size(x)):
            error[j] = abs(np.log(x[j]) - fast_approx_ln(x[j], i))
        print(error[1], error[4], error[10])
        plt.scatter(x, error, color=colors[i-2], label=f'iteration {i}', marker='o', s=5)
    plt.xlabel('x')
    plt.xlim(0, 20)
    plt.ylabel('y')
    plt.yscale('log')
    plt.ylim(10**-19, 10**-5)
    plt.legend()


main()
plt.show()

