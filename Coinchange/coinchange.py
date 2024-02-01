import sys
import time as t

LIMIT = 2**31 - 1
sys.setrecursionlimit(LIMIT)


MEMOIZATION = [-1] * 10000
VALUES = [1, 5, 6, 7]


def reset_memoization():
    global MEMOIZATION
    MEMOIZATION = [-1] * 10000


def coin_change_memo(n):
    global MEMOIZATION
    if n < 0:
        return 100000000
    elif n == 0:
        return 0
    elif MEMOIZATION[n] != -1:
        return MEMOIZATION[n]
    else:
        min_tot = min(coin_change_memo(n - VALUES[i]) + 1 for i in range(len(VALUES)))
        MEMOIZATION[n] = min(n, min_tot)
        return MEMOIZATION[n]

def coin_change_exhaustive(n):
    if n < 0:
        return 100000000
    elif n == 0:
        return 0
    else:
        min_temp = min(coin_change_exhaustive(n - VALUES[i]) + 1 for i in range(len(VALUES)))
        return min(n, min_temp)
    
def bottom_up(n):
    table = [0] * (n + 1)
    for i in range(1, n + 1):
        min_val = float('inf')
        for j in range(len(VALUES)):
            if i >= VALUES[j]:
                min_val = min(min_val, table[i - VALUES[j]] + 1)
        table[i] = min_val
    return table[n]

def test_limits_addition_memo():
    global VALUES
    VALUES = [1, 5, 6, 7]
    times = []
    n = 10
    delta = 0
    while delta < 1:  # 1 second
        t0 = t.time()
        number = coin_change_memo(n)
        delta = t.time() - t0
        reset_memoization()
        times.append((n, delta, number))
        n += 1
    return times


def test_limits_multiplication_memo():
    global VALUES
    VALUES = [1, 5, 6, 7]
    times = []
    n = 10
    delta = 0
    while delta < 1:  # 1 second
        t0 = t.time()
        number = coin_change_memo(n)
        delta = t.time() - t0
        reset_memoization()
        times.append((n, delta, number))
        n *= 2
    return times


def test_limits_addition(algo=coin_change_exhaustive, factor=1):
    global VALUES
    VALUES = [1, 5, 6, 7]
    times = []
    n = 10
    delta = 0
    while delta < 1:  # 1 second
        # print("add", n, delta)
        t0 = t.time()
        number = algo(n)
        delta = t.time() - t0
        times.append((n, delta, number))
        n += factor
    return times


def test_limits_multiplication(algo=coin_change_exhaustive):
    global VALUES
    VALUES = [1, 5, 6, 7]
    times = []
    n = 10
    delta = 0
    while delta < 1:  # 1 second
        # print("multi", n, delta)
        t0 = t.time()
        number = algo(n)
        delta = t.time() - t0
        times.append((n, delta, number))
        n *= 2
    return times


def plot_times(timesadd, timesmult, title):
    import matplotlib.pyplot as plt

    x = [t[0] for t in timesadd]
    y = [t[1] for t in timesadd]
    x_mult = [t[0] for t in timesmult]
    y_mult = [t[1] for t in timesmult]
    plt.title(title)
    plt.plot(x, y, color="red", marker="o", linestyle="solid")
    plt.plot(x_mult, y_mult, color="blue", marker="o", linestyle="solid")
    plt.legend(["Addition", "Multiplication"])
    plt.xlabel("n")
    plt.ylabel("time")
    plt.savefig(title + '.png')
    plt.show()





def ask_user_input():
    global VALUES
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    VALUES = [1, a, b, c]
    return n


def main():
    n = ask_user_input()
    print(coin_change_memo(n))
    print(coin_change_exhaustive(n))
    print(bottom_up(n))


def test(algo):
    timesadd = test_limits_addition(algo, factor=10000)
    timesmult = test_limits_multiplication(algo)
    plot_times(timesadd, timesmult, "Coin Change Bottom Up")

test(bottom_up)