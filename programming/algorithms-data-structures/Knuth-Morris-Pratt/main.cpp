//
// Created by Drapegnik on 19.03.14.
//
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
ifstream fin("Knuth-Morris-Pratt/input.txt");
ofstream fout("Knuth-Morris-Pratt/output.txt");

vector<int> prefix(string s) {
  int n = s.length();
  vector<int> pi(n, 0);
  for (int i = 1; i < n; i++) {
    int j = pi[i - 1];

    while (j > 0 && s[i] != s[j]) {
      j = pi[j - 1];
    }

    if (s[i] == s[j]) {
      j++;
    }

    pi[i] = j;
  }
  return pi;
}

int main() {
  string s;
  fin >> s;
  s += '#';
  int n = s.length();
  vector<int> pi = prefix(s);
  vector<vector<int> > aut(n, vector<int>(26));

  for (int i = 0; i < n; i++) {
    for (char c = 'a'; c <= 'z'; c++) {
      if (i > 0 && c != s[i]) {
        aut[i][c - 'a'] = aut[pi[i - 1]][c - 'a'];
      } else {
        aut[i][c - 'a'] = i + (c == s[i]);
      }
    }
  }

  long long ans = 0;
  int p1 = 0, p2 = 0;
  while (!fin.eof()) {
    p1 = p2;
    char x;
    fin >> x;
    p2 = aut[p1][int(x - 'a')];
    if (p2 == n - 1) {
      ans++;
    }
  }
  fout << ans;
  return 0;
}
