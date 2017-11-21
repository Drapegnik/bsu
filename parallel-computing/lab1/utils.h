//
// Created by Ivan Pazhitnykh on 9/22/17.
//

#ifndef LAB1_UTILS_H
#define LAB1_UTILS_H

#include <iostream>
#include <random>
#include <chrono>
#include <iomanip>

using namespace std;

typedef vector<vector<int>> matrix_t;
typedef chrono::high_resolution_clock hr_clock;
typedef chrono::milliseconds ms;
typedef unsigned long ulong;

class Timer {
 private:
  static hr_clock::time_point start_time;

 public:
  static void start();

  static double end();

  static void print();
};

int get_random_number();

matrix_t get_matrix(ulong rows, ulong cols);

ostream& print_matrix(matrix_t& v);

#endif //LAB1_UTILS_H
