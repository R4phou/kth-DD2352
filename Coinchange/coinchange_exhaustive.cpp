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

float LIMIT = 1;
int VALUES[] = {1, 5, 6, 7};

int coin_change(int n) {
    if (n < 0) {
        return 100000000;
    } else if (n == 0) {
        return 0;
    } else {
        int min_tot = std::numeric_limits<int>::max();
        for (int i = 0; i < sizeof(VALUES) / sizeof(VALUES[0]); ++i) {
            min_tot = std::min(min_tot, coin_change(n - VALUES[i]) + 1);
        }
        return std::min(n, min_tot);
    }
}


std::vector<coin_try> test_limits_addition() {
    std::vector<coin_try> times;
    coin_try coin;
    int n = 5;
    double delta = 0;
    while (delta < LIMIT) {
        clock_t t0 = clock();
        int number = coin_change(n);
        delta = (clock() - t0) / static_cast<double>(CLOCKS_PER_SEC);
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
    int n = 2;
    double delta = 0;
    while (delta < (int)LIMIT/2) {
        clock_t t0 = clock();
        int number = coin_change(n);
        delta = (clock() - t0) / static_cast<double>(CLOCKS_PER_SEC);
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
    int n = 20;
    clock_t t0 = clock();
    int number = coin_change(n);
    double delta = (clock() - t0) / static_cast<double>(CLOCKS_PER_SEC);
    coin_try coin;
    coin.amount = n;
    coin.result = number;
    coin.time = delta;
    std::cout << "Test for n = " << n << " -> " << coin_change(n) << std::endl;


    // auto times_add = test_limits_addition();
    // std::cout << "Times_Add done" << std::endl;
    // print_in_file(times_add, "./exhaust_add.txt");

    auto times_mult = test_limits_multiplication();
    std::cout << "Times_Mult done" << std::endl;
    print_in_file(times_mult, "./exhaust_mult.txt");

    return 0;
}
