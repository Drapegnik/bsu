//
// Created by Drapegnik on 05.02.14.
//
#include <vector>
#include <fstream>

using namespace std;
ifstream fin("combination_generating/input.txt");
ofstream fout("combination_generating/output.txt");
int n, k;
vector<int> v;

bool cnk() {
  for (int i = k - 1; i >= 0; i--) {
    if (v[i] < n - k + i + 1) {
      v[i]++;
      for (int j = i + 1; j < k; j++) {
        v[j] = v[j - 1] + 1;
      }
      return true;
    }
  }
  return false;
}

int main() {
  fin >> n >> k;
  v = vector<int>(k, 0);

  for (int i = 0; i < k; i++) {
    v[i] = i + 1;
    fout << v[i] << " ";
  }
  fout << endl;

  while (cnk() == true) {
    for (int i = 0; i < k; i++) {
      fout << v[i] << " ";
    }
    fout << endl;
  }
  return 0;
}
