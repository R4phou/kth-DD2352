#include <iostream>
#include <vector>
#include <limits>
#include <ctime>
#include <fstream>


struct coin_try {
    int amount;
    int result;
    double time;
};

float LIMIT = 0.001;
int VALUES[] = {1, 5, 6, 7};
std::vector<int> MEMOIZATION(10000, -1);

void reset_memoization() {
    std::fill(MEMOIZATION.begin(), MEMOIZATION.end(), -1);
}

int coin_change_memo(int n) {
    if (n < 0) {
        return 100000000;
    } else if (n == 0) {
        return 0;
    } else if (MEMOIZATION[n] != -1) {
        return MEMOIZATION[n];
    } else {
        int min_tot = std::numeric_limits<int>::max();
        for (int i = 0; i < sizeof(VALUES) / sizeof(VALUES[0]); ++i) {
            min_tot = std::min(min_tot, coin_change_memo(n - VALUES[i]) + 1);
        }
        MEMOIZATION[n] = std::min(n, min_tot);
        return MEMOIZATION[n];
    }
}


std::vector<coin_try> test_limits_addition() {
    std::vector<coin_try> times;
    coin_try coin;
    int n = 5;
    double delta = 0;
    while (delta < (int) LIMIT/2) {
        clock_t t0 = clock();
        int number = coin_change_memo(n);
        delta = (clock() - t0) / static_cast<double>(CLOCKS_PER_SEC);
        reset_memoization();
        coin.amount = n;
        coin.result = number;
        coin.time = delta;
        times.push_back(coin);
        n += 1;
    }
    return times;
}

std::vector<coin_try> test_limits_multiplication() {
    std::vector<coin_try> times;
    coin_try coin;
    int n = 5;
    double delta = 0;
    while (delta < LIMIT) {
        clock_t t0 = clock();
        int number = coin_change_memo(n);
        delta = (clock() - t0) / static_cast<double>(CLOCKS_PER_SEC);
        reset_memoization();
        coin.amount = n;
        coin.result = number;
        coin.time = delta;
        times.push_back(coin);
        n *= 2;
    }
    return times;
}



void print_in_file(std::vector<coin_try> times, std::string title){
    // Print the results in a file
    std::ofstream file;
    file.open(title);
    file << "amount,result,time\n";
    for (auto coin : times) {
        file << coin.amount << "," << coin.result << "," << coin.time << "\n";
    }
    file.close();
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    int n = 500;
    clock_t t0 = clock();
    int number = coin_change_memo(n);
    double delta = (clock() - t0) / static_cast<double>(CLOCKS_PER_SEC);
    coin_try coin;
    coin.amount = n;
    coin.result = number;
    coin.time = delta;
    std::cout << "Test for n = " << n << " -> " << coin_change_memo(n) << std::endl;
    print_in_file({coin}, "./memo_add.txt");
    auto times_memo_add = test_limits_addition();
    std::cout << "Times_memo_Add done" << std::endl;
    auto times_memo_mult = test_limits_multiplication();
    std::cout << "Times_memo_Mult done" << std::endl;
    print_in_file(times_memo_add, "./memo_add.txt");
    print_in_file(times_memo_mult, "./memo_mult.txt");
    // Call the plot_times function if you have a C++ plotting library or use an external tool.
    return 0;
}
