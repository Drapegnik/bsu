//
// Created by Drapegnik on 20.01.14.
//
#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("Dijkstra's/input.txt");
ofstream fout("Dijkstra's/output.txt");

int main() {
  int n, f, s, a[101][101], d[101], p[101];
  bool us[101];
  const int c = INT_MAX;

  fin >> n >> s >> f;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      fin >> a[i][j];
    }
  }

  for (int i = 0; i <= n; i++) {
    us[i] = false;
    d[i] = c;
  }

  d[s - 1] = 0;
  p[s - 1] = -1;

  while (true) {
    int num = n;
    for (int j = 0; j < n; j++) {
      if ((!us[j]) && (d[j] < d[num])) {
        num = j;
      }
    }

    if (num == n) { break; }

    us[num] = true;

    for (int j = 0; j < n; j++) {
      if (a[num][j] > 0) {
        if (d[num] + a[num][j] < d[j]) {
          d[j] = d[num] + a[num][j];
          p[j] = num;
        }
      }
    }
  }

  if (d[f - 1] == c) {
    fout << -1;
  } else {
    fout << d[f - 1];
  }

  return 0;
}
