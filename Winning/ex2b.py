import sys
import time as t
import numpy as np

LIMIT = 2**31 - 1
sys.setrecursionlimit(LIMIT)


P = 0.99
K = -1
MEMOIZATION = -1


def winning_streak_memo(x, y):
    global MEMOIZATION
    if MEMOIZATION[y][x] != -1:
        return MEMOIZATION[y][x]
    if y == 0:
        MEMOIZATION[y][x] = 1
        return 1
    if x == 0 and y > 0:
        MEMOIZATION[y][x] = 0
        return 0
    if x >= 1 and y >= 1:
        MEMOIZATION[y][x] = P * winning_streak_memo(x - 1, y - 1) + (
            1 - P
        ) * winning_streak_memo(x - 1, K)
        return MEMOIZATION[y][x]


def find_limit():
    global K, P, MEMOIZATION
    results = []
    n = 2
    delta = 0
    while delta < 1:  # 1 second
        K = n // 2
        MEMOIZATION = np.full((K + 1, n + 1), -1, float)
        t0 = t.time()
        number = winning_streak_memo(n, K)
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
    while delta < 1:  # 1 second
        K = n // 2
        MEMOIZATION = np.full((K + 1, n + 1), -1, float)
        t0 = t.time()
        number = winning_streak_memo(n, K)
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
    plt.title("Memoization Winning Streak")
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
    print("results: ", results)
    plot_results(results, results_mult)
    print_results_in_file(results, "./outputs/ex1b_results_add.csv")
    print_results_in_file(results_mult, "./outputs/ex1b_results_mult.csv")


main()
