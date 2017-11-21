//
// Created by Ivan Pazhitnykh on 9/22/17.
//

#include "lab1.h"

const string USAGE = "./lab1 -n <rows> -m <cols> -r <block_size> [-o <out_file>='output.txt']";

int main(int argc, char* argv[]) {
  if (argc < 7) {
    cerr << "Error. Usage is:" << endl;
    cerr << USAGE << endl;
    return 1;
  }

  int n1, n2, block_size;
  string filename = "output.txt";

  for (int i = 1; i < argc; i += 2) {
    if (string(argv[i]) == "-n") {
      n1 = atoi(argv[i + 1]);
    } else if (string(argv[i]) == "-m") {
      n2 = atoi(argv[i + 1]);
    } else if (string(argv[i]) == "-r") {
      block_size = atoi(argv[i + 1]);
    } else if (string(argv[i]) == "-o") {
      filename = argv[i + 1];
    } else {
      cerr << USAGE << endl;
      return 1;
    }
  }

  int n3 = n1;
  fstream fout;
  fout.open(filename, fstream::out | fstream::app);
  omp_set_dynamic(0);
  omp_set_num_threads(8);

  matrix_t m1 = get_matrix(n1, n2);
  matrix_t m2 = get_matrix(n2, n3);
  matrix_t m3(n1, vector<int>(n3, 0));

  fout << block_size << " ";

  // 0 - sequential, 1 - first for parallel, 2 - second for parallel
  for (int parallel_num = 0; parallel_num <= 2; parallel_num++) {
    Timer::start();
    if (block_size == 1) {
      linear_multiply(m1, m2, m2, parallel_num);
    } else {
      block_multiply(m1, m2, m3, block_size, parallel_num);
    }
    fout << Timer::end() << " ";
  }
  fout << endl;
  return 0;
}

void linear_multiply(
    matrix_t& m1, matrix_t& m2, matrix_t& result, int parallel_num
) {
  ulong n1 = m1.size();
  ulong n2 = m1[0].size();
  ulong n3 = m2[0].size();

#pragma omp parallel for if (parallel_num == 1)
  for (int i = 0; i < n1; i++) {
#pragma omp parallel for if (parallel_num == 2)
    for (int j = 0; j < n3; j++) {
      for (int k = 0; k < n2; k++) {
        result[i][j] += m1[i][k] * m2[k][j];
      }
    }
  }
  return;
}

void block_multiply(
    matrix_t& m1, matrix_t& m2, matrix_t& result,
    int block_size, int parallel_num
) {
  ulong n1 = m1.size();
  ulong n2 = m2[0].size();
  ulong n3 = m1[0].size();
  ulong q1 = n1 / block_size;
  ulong q2 = n2 / block_size;
  ulong q3 = n3 / block_size;

#pragma omp parallel for if (parallel_num == 1)
  for (int i1 = 0; i1 < q1; i1++) {
#pragma omp parallel for if (parallel_num == 2)
    for (int j1 = 0; j1 < q2; j1++) {
      for (int k1 = 0; k1 < q3; k1++) {
        for (int i2 = 1; i2 < block_size; i2++) {
          for (int j2 = 1; j2 < block_size; j2++) {
            for (int k2 = 1; k2 < block_size; k2++) {
              int i = i1 * block_size + i2;
              int j = j1 * block_size + j2;
              int k = k1 * block_size + k2;
              result[i][j] += m1[i][k] * m2[k][j];
            }
          }
        }
      }
    }
  }
  return;
}
