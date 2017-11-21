//
// Created by Ivan Pazhitnykh on 9/22/17.
//

#include "utils.h"

hr_clock::time_point Timer::start_time = hr_clock::now();

void Timer::start() {
  start_time = hr_clock::now();
}

double Timer::end() {
  auto end_time = hr_clock::now();
  return chrono::duration_cast<ms>(end_time - start_time).count() / 1000.;
}

void Timer::print() {
  cout << "elapsed: " << setprecision(3) << end() << " s" << endl;
}

/*
 * generate random number in [-100, 100]
 */
int get_random_number() {
  return (rand() % 200) - 100;
}

matrix_t get_matrix(ulong rows, ulong cols) {
  matrix_t v(rows, vector<int>(cols));
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      v[i][j] = get_random_number();
    }
  }
  return v;
}

ostream& print_matrix(matrix_t& v) {
  for (int i = 0; i < v.size(); i++) {
    for (int j = 0; j < v[i].size(); j++) {
      cout << v[i][j] << " ";
    }
    cout << endl;
  }

  return cout;
}
