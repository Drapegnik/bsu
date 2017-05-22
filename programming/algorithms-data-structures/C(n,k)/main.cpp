//
// Created by Drapegnik on 18.03.14.
//
#include <vector>
#include <fstream>

using namespace std;
ifstream fin("C(n,k)/input.txt");
ofstream fout("C(n,k)/output.txt");

int main() {
  int n, k;
  fin >> n >> k;
  vector<int> a(n + 1, 1);
  for (int i = 1; i < n; i++)
    for (int j = i; j >= 1; j--)
      a[j] += a[j - 1];

  fout << a[k];
  return 0;
}
