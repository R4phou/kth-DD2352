import sys

LIMIT = 2**31 - 1
sys.setrecursionlimit(LIMIT)


P = 0.99
K = -1
MEMOIZATION = -1


def winning_streak_improved(x):
    if x < K:
        return 0
    if x == K:
        return P**K
    else:  # if x >= k+1
        return winning_streak_improved(x - 1) + P**K * (1 - P) * (
            1 - winning_streak_improved(x - 1 - K)
        )


def winning_streak_imp_memo(x):
    global MEMOIZATION
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


def ask_user_input():
    global K, P, MEMOIZATION
    n = int(input())
    K = int(input())
    P = float(input())
    MEMOIZATION = [-1] * (n + 1)
    print(round(winning_streak_imp_memo(n), 6))
    # print(round(winning_streak_improved(n), 6))


def main():
    global K, P, MEMOIZATION
    n = 4  # number of games
    K = 2  # number of consecutive wins
    P = 0.7  # probability of winning a game
    MEMOIZATION = [-1] * (n + 1)
    print(float(winning_streak_imp_memo(n)))
    print(float(winning_streak_improved(n)))


ask_user_input()
# main()
