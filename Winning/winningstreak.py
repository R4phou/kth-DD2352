


P = -1
K = -1

def winning_streak(x,y):
    if y == 0:
        return 1
    if x == 0 and y > 0:
        return 0
    if x>= 1 and y >= 1:
        return P*winning_streak(x-1,y-1) + (1-P) * winning_streak(x-1,K)
    

def main():
    global K, P
    n = 20  # number of games
    K = 4 # number of consecutive wins
    P = 0.42  # probability of winning a game
    print(winning_streak(n,K))

main()