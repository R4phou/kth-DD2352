import matplotlib.pyplot as plt
import numpy as np 


def plot_memo():
    # amount,result,time
    addition = np.genfromtxt('./outputs/ex2d_add_cpp.csv', delimiter=',', skip_header=1)

    amount_add = [t[0] for t in addition]
    time_add = [t[2] for t in addition]
    plt.title("Winning Streak Improved")
    plt.plot(amount_add, time_add, color="red")
    plt.xlabel("n")
    plt.ylabel("time")
    plt.savefig('WinningStreak.png')
    plt.show()

plot_memo()