//
// Created by Drapegnik on 19.03.14.
//
#include <fstream>

using namespace std;
ifstream fin("brute_force/input.txt");
ofstream fout("brute_force/output.txt");

int main() {
  int n;
  fin >> n;
  int m = 1 << n;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      int x = (i >> j) & 1;
      fout << x;
    }
    fout << endl;
  }
  return 0;
}
