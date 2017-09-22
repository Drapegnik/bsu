//
// Created by Ivan Pazhitnykh on 9/22/17.
//

#include "lab1.h"

int main() {
  const int N = 100;
  const int n1 = N, n2 = N, n3 = N;
  matrix_t m1 = get_matrix(n1, n2);
  matrix_t m2 = get_matrix(n2, n3);

  Timer::start();
  matrix_t m3 = multiply(m1, m2);
  Timer::print();

  return 0;
}

matrix_t multiply(matrix_t& m1, matrix_t& m2) {
  int n1 = m1.size();
  int n2 = m1[0].size();
  int n3 = m2[0].size();
  matrix_t result(n1, vector<int>(n3));

  for (int i = 0; i < n1; i++) {
    for (int j = 0; j < n3; j++) {
      int tmp = 0;
      for (int k = 0; k < n2; k++) {
        tmp += m1[i][k] * m2[k][j];
      }
      result[i][j] = tmp;
    }
  }

  return result;
}
