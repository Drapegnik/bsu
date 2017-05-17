//
// Created by Drapegnik on 23.01.14.
//
#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("A+B/input.txt");
ofstream fout("A+B/output.txt");

int main() {
  int k1, k2, a[101] = {}, b[101] = {}, c = 0;
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

  if (k1 > k2) {
    for (int i = k2; i <= k1; i++) {
      b[i] = 0;
    }
  } else {
    for (int i = k1; i <= k2; i++) {
      a[i] = 0;
    }
    k1 = k2;
  }

  for (int i = 0; i < k1; i++) {
    c = c + a[i] + b[i];
    a[i] = c % 10;
    c = c / 10;
  }

  if (c > 0) {
    k1++;
    a[k1 - 1] = c;
  }

  for (int i = k1 - 1; i >= 0; i--) {
    fout << a[i];
  }
  return 0;
}
