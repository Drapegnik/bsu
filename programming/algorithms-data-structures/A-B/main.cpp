//
// Created by Drapegnik on 14.01.14.
//
#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("A-B/input.txt");
ofstream fout("A-B/output.txt");

int main() {
  int k1, k2, a[101] = {}, b[101] = {}, c;
  string s1, s2;
  fin >> s1 >> s2;
  k1 = s1.length();
  k2 = s2.length();

  for (int i = k1 - 1; i >= 0; i--) {
    a[k1 - i - 1] = s1[i] - '0';
  }

  for (int i = k2 - 1; i >= 0; i--) {
    b[k2 - i - 1] = s2[i] - '0';
  }

  for (int i = 0; i < k1; i++) {
    c = a[i] - b[i];

    if (c < 0) {
      a[i] = 10 + c;
      a[i + 1]--;
    } else {
      a[i] = c;
    }
  }

  while (a[k1 - 1] == 0) { k1--; }

  if (k1 == 0) { fout << 0; }

  for (int i = k1 - 1; i >= 0; i--) {
    fout << a[i];
  }
  return 0;
}
