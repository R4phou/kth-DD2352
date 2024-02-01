import sys
import time as t

LIMIT = 2**31 - 1
sys.setrecursionlimit(LIMIT)


P = 0.99
K = -1
MEMOIZATION = -1


def winning_streak_memo(x,y):
    global MEMOIZATION
    if MEMOIZATION[y][x] != -1:
        return MEMOIZATION[y][x]
    if y == 0:
        MEMOIZATION[y][x] = 1
        return 1
    if x == 0 and y > 0:
        MEMOIZATION[y][x] = 0
        return 0
    if x>= 1 and y >= 1:
        MEMOIZATION[y][x] = P*winning_streak_memo(x-1,y-1) + (1-P) * winning_streak_memo(x-1,K)
        return MEMOIZATION[y][x]



def find_limit():
    global K, P, MEMOIZATION
    results = []
    n = 2 
    delta = 0
    while delta < 1:  # 1 second
        K = n//2
        MEMOIZATION = [[-1 for i in range(n+1)] for j in range(K+1)]
        t0 = t.time()
        number = winning_streak_memo(n,K)
        delta = t.time() - t0
        # print(n, delta, number)
        n += 5
        results.append((n, delta, number))
    return results


def plot_results(results):
    import matplotlib.pyplot as plt
    x = [i[0] for i in results]
    y = [i[1] for i in results]
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,)
    plt.show()


def main():
    results = find_limit()
    print("results: ", results)
    plot_results(results)

main()
