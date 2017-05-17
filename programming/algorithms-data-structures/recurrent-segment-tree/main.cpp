//
// Created by Drapegnik on 17.03.14.
//
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
ifstream fin("recurrent-segment-tree/input.txt");

int const INF = -1;
vector<int> a;

int search(int l, int r) {
  if (l > r) {
    return INF;   // INF - neutral
  }
  if (l == r) {
    return a[l];
  }
  if (l % 2 == 0) {
    if (r % 2 != 0) {
      return search(l / 2, r / 2);
    } else {
      return max(a[r], search(l / 2, (r - 1) / 2));
    }
  } else {
    if (r % 2 != 0) {
      return max(a[l], search((l + 1) / 2, r));
    } else {
      return max(a[l], max(a[r], search((l + 1) / 2, (r - 1) / 2)));
    }

  }
}

int main() {
  int n;
  fin >> n;
  int sz = n;

  while (sz & (sz - 1)) {
    sz++;
  }

  a = vector<int>(2 * sz, INF); // INF - neutral
  for (int i = sz; i < sz + n; i++) {
    fin >> a[i];
  }

  for (int i = sz - 1; i > 0; i--) {
    a[i] = max(a[i * 2], a[i * 2 + 1]);
  }

  int l, r;
  cin >> l >> r;
  cout << search(l + sz - 1, r + sz - 1);
  return 0;
}
