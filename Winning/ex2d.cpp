#include <iostream>
#include <vector>
#include <limits>
#include <ctime>
#include <fstream>
#include <cmath>


struct winning_streak_try {
    int n;
    float result;
    double time;
};

float LIMIT = 1;
float P = 0.99;
int K = -1;
std::vector<float> MEMOIZATION(1000, -1);

void reset_memoization(int n) {
    MEMOIZATION = std::vector<float>(n, -1);
}

float winning_streak(int x){
    if (MEMOIZATION[x] == -1){ 
        if (x < K){
            MEMOIZATION[x] = 0;
        } else if (x == K){
            MEMOIZATION[x] = std::pow(P, K);
        } else {
            MEMOIZATION[x] = winning_streak(x-1) + std::pow(P, K)* (1-P)* (1-winning_streak(x-K-1));
        }
    }
    return MEMOIZATION[x];
}

std::vector<winning_streak_try> test_limits_addition() {
    std::vector<winning_streak_try> times;
    winning_streak_try current;
    int n = 2000000;
    K = 1000000;
    double delta = 0;
    while (delta < LIMIT) {
        reset_memoization(n);
        clock_t t0 = clock();
        current.result = winning_streak(n);
        delta = (clock() - t0) / static_cast<double>(CLOCKS_PER_SEC);
        current.n = n;
        current.time = delta;
        if (delta != 0){
            times.push_back(current);
        }
        n += 1000000;
        K = (int) n/2;
        if (n % 1000 == 0) {
            std::cout << n<< " | ";
            std::cout << delta << " s" << std::endl;
        }
    }
    return times;
}


void print_in_file(std::vector<winning_streak_try> times, std::string title){
    // Print the results in a file
    std::ofstream file;
    file.open(title);
    file << "amount,result,time\n";
    for (auto data : times) {
        file << data.n << "," << data.result << "," << data.time << "\n";
    }
    file.close();
}

void test_function(){
    int n = 15;
    K = (int) n/2;
    P = 0.99;
    std::cout << "n = " << n <<  " K =" << K <<" result: " << winning_streak(n) << std::endl;
}

int main() {
    std::cout << "Starting tests" << std::endl;
    std::vector<winning_streak_try> times = test_limits_addition();
    print_in_file(times, "./outputs/ex2d_add_cpp.csv");
    // test_function();
    return 0;
}
