//
// Created by Drapegnik on 28.02.14.
//
#include <fstream>
#include <vector>

using namespace std;
ifstream fin("A-div-n/input.txt");
ofstream fout("A-div-n/output.txt");

int main() {
  const int base = 1000 * 1000 * 1000;
  int ost = 0, n, k;
  string s;
  fin >> s >> n;
  k = s.length();
  vector<int> a;

  for (int i = k; i > 0; i -= 9) {
    if (i < 9) {
      a.push_back(atoi(s.substr(0, i).c_str()));
    } else {
      a.push_back(atoi(s.substr(i - 9, 9).c_str()));
    }
  }


  for (int i = (int) a.size() - 1; i >= 0; --i) {
    long long cur = a[i] + ost * 1ll * base;
    a[i] = int(cur / n);
    ost = int(cur % n);
  }

  while (a.size() > 1 && a.back() == 0) {
    a.pop_back();
  }

  if (a.empty()) {
    fout << 0;
  } else {
    fout << a.back();
  }

  for (int i = (int) a.size() - 2; i >= 0; --i) {
    fout << a[i];
  }

  fout << endl << ost;
  return 0;
}
