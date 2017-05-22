//
// Created by Drapegnik on 26.12.13.
//
#include <fstream>

using namespace std;
ifstream fin("Floyds/input.txt");
ofstream fout("Floyds/output.txt");

int main() {
  int n, a[100][100];
  fin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      fin >> a[i][j];
    }
  }

  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if ((j != k) && (i != k)) {
          a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
        }
      }
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      fout << a[i][j] << " ";
    }
    fout << endl;
  }

  return 0;
}
