import matplotlib.pyplot as plt
import numpy as np 


def plot_memo():
    # amount,result,time
    addition = np.genfromtxt('./memo_add.txt', delimiter=',', skip_header=1)
    print(addition)
    multiplication = np.genfromtxt('./memo_mult.txt', delimiter=',', skip_header=1)
    print(multiplication)

    amount_add = [t[0] for t in addition]
    time_add = [t[2] for t in addition]
    amount_mult = [t[0] for t in multiplication]
    time_mult = [t[2] for t in multiplication]
    plt.title("Coin Change Memoisation")
    plt.plot(amount_add, time_add, color="red", marker="o", linestyle="solid")
    plt.plot(amount_mult, time_mult, color="blue", marker="o", linestyle="solid")
    plt.legend(["Addition", "Multiplication"])
    plt.xlabel("n")
    plt.ylabel("time")
    plt.savefig('memo.png')
    plt.show()


def plot_exhaust():
    # amount,result,time
    addition = np.genfromtxt('./exhaust_add.txt', delimiter=',', skip_header=1)
    print(addition)
    multiplication = np.genfromtxt('./exhaust_mult.txt', delimiter=',', skip_header=1)
    print(multiplication)

    amount_add = [t[0] for t in addition]
    time_add = [t[2] for t in addition]
    amount_mult = [t[0] for t in multiplication]
    time_mult = [t[2] for t in multiplication]
    plt.title("Coin Change Exhaustive")
    plt.plot(amount_add, time_add, color="red", marker="o", linestyle="solid")
    plt.plot(amount_mult, time_mult, color="blue", marker="o", linestyle="solid")
    plt.legend(["Addition", "Multiplication"])
    plt.xlabel("n")
    plt.ylabel("time")
    plt.savefig('exhaust.png')
    plt.show()


plot_exhaust()