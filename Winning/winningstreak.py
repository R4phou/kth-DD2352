P = -1
K = -1
MEMOIZATION = -1

def winning_streak(x,y):
    if y == 0:
        return 1
    if x == 0 and y > 0:
        return 0
    if x>= 1 and y >= 1:
        return P*winning_streak(x-1,y-1) + (1-P) * winning_streak(x-1,K)
    
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

def ask_user_input():
    global K, P
    n = int(input())
    K = int(input())
    P = float(input())
    print(winning_streak(n,K))

def ask_user_input_memo():
    global K, P, MEMOIZATION
    n = int(input())
    K = int(input())
    P = float(input())
    MEMOIZATION = [[-1 for i in range(n+1)] for j in range(K+1)]
    print(winning_streak_memo(n,K))

def main():
    global K, P, MEMOIZATION
    n = 20  # number of games
    K = 4 # number of consecutive wins
    P = 0.42  # probability of winning a game
    MEMOIZATION = [[-1 for i in range(n+1)] for j in range(K+1)]
    print(winning_streak(n,K))

# main()
# ask_user_input()    
ask_user_input_memo()    