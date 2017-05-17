//
// Created by Drapegnik on 22.03.14.
//
#include <fstream>
#include <vector>

using namespace std;
ifstream fin("Aho-Corasick/input.txt");
ofstream fout("Aho-Corasick/output.txt");

struct vert {
  int next[26];
  bool fl;
};

vector<vert> t;
int sz = 0;
vert x;


void add_string(string s) {
  int v = 0;
  for (int i = 0; i < s.length(); i++) {
    char c = s[i] - 'a';
    if (t[v].next[c] == -1) {
      t.push_back(x);
      t[v].next[c] = sz;
      sz++;
    }
    v = t[v].next[c];
  }
  t[v].fl = true;
}

bool search_string(string s) {
  int v = 0;
  for (int i = 0; i < s.length(); i++) {
    char c = s[i] - 'a';

    if (t[v].next[c] == -1) { return false; }

    v = t[v].next[c];
  }

  return (t[v].fl == true);
}

int main() {
  int n, m;
  fin >> n;

  x.fl = false;
  for (int i = 0; i < 26; i++) {
    x.next[i] = -1;
  }

  t.push_back(x);
  sz = 1;

  for (int i = 0; i < n; i++) {
    string s;
    fin >> s;
    add_string(s);
  }

  fin >> m;

  for (int j = 0; j < m; j++) {
    string s;
    fin >> s;
    bool b = search_string(s);
    if (b) {
      fout << "YES" << endl;
    } else {
      fout << "NO" << endl;
    }
  }
  return 0;
}
