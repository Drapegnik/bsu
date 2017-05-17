//
// Created by Drapegnik on 18.03.14.
//
#include <iostream>

using namespace std;

int n, a;

int bin_pow(int a, int n) {
  if (n == 0) { return 1; }

  if (n % 2 == 1) {
    return bin_pow(a, n - 1) * a;
  } else {
    int b = bin_pow(a, n / 2);
    return b * b;
  }
}

int main() {
  cin >> a >> n;
  cout << bin_pow(a, n) << endl;

  int res = 1;
  while (n > 0) {
    if (n % 2 != 0) {
      res *= a;
    }
    a *= a;
    n /= 2;;
  }
  cout << res << endl;
  return 0;
}
