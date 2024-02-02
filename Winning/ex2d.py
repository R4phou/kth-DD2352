import sys
import time as t
import numpy as np

LIMIT = 2**31 - 1
sys.setrecursionlimit(LIMIT)


P = 0.99
K = -1
MEMOIZATION = -1
I = 1


def winning_streak_imp_memo(x):
    global MEMOIZATION, I
    I += 1
    if x < K:
        MEMOIZATION[x] = 0
        return 0
    if x == K:
        MEMOIZATION[x] = P**K
        return MEMOIZATION[x]
    if MEMOIZATION[x] != -1:
        return MEMOIZATION[x]
    else:  # if x >= k+1
        MEMOIZATION[x] = winning_streak_imp_memo(x - 1) + P**K * (1 - P) * (
            1 - winning_streak_imp_memo(x - K - 1)
        )
        return MEMOIZATION[x]


def find_limit():
    global K, P, MEMOIZATION
    results = []
    n = 2
    delta = 0
    while delta < 1 and n < 4332:  # 1 second
        K = n // 2
        MEMOIZATION = np.full(n + 1, -1, float)
        print(n)
        t0 = t.time()
        number = winning_streak_imp_memo(n)
        delta = t.time() - t0
        # print(n, delta, number)
        n += 10
        results.append((n, delta, number))
    return results


def find_limit_mult():
    global K, P, MEMOIZATION
    results = []
    n = 2
    delta = 0
    while delta < 1 and n < 4332:  # 1 second
        K = n // 2
        print(n)
        MEMOIZATION = np.full(n + 1, -1, float)
        t0 = t.time()
        number = winning_streak_imp_memo(n)
        delta = t.time() - t0
        # print(n, delta, number)
        n *= 2
        results.append((n, delta, number))
    return results


def plot_results(results, results_mult):
    import matplotlib.pyplot as plt

    x = [i[0] for i in results]
    y = [i[1] for i in results]
    x_mult = [i[0] for i in results_mult]
    y_mult = [i[1] for i in results_mult]
    plt.title("Memoization Winning Streak improved")
    plt.plot(x, y, color="green", label="n + 10", marker="o", linestyle="solid")
    plt.plot(x_mult, y_mult, color="red", label="n * 2", marker="o", linestyle="solid")
    plt.xlabel("n")
    plt.ylabel("time (s)")
    plt.legend(["Addition", "Multiplication"])
    plt.show()


def print_results_in_file(results, file):
    np.savetxt(file, results, delimiter=",", fmt="%s")


def main():
    results = find_limit()
    results_mult = find_limit_mult()
    # print("results: ", results)
    plot_results(results, results_mult)
    print(I)
    print_results_in_file(results, "./outputs/ex2d_results_add.csv")
    print_results_in_file(results_mult, "./outputs/ex2d_results_mult.csv")


def plot_from_file():
    import matplotlib.pyplot as plt

    results = np.genfromtxt("./outputs/ex2d_results_add.csv", delimiter=",")
    results_mult = np.genfromtxt("./outputs/ex2d_results_mult.csv", delimiter=",")
    plot_results(results, results_mult)


# main()
plot_from_file()
