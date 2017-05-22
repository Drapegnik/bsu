//
// Created by Drapegnik on 05.03.14.
//
#include <fstream>
#include <vector>

using namespace std;
ifstream fin("Dinic's/input.txt");
ofstream fout("Dinic's/output.txt");

const int INF = INT_MAX;
int n, s, t;
vector<vector<int> > c, f;
vector<int> d, ptr, q;

bool bfs() {
  int qh = 0, qt = 0;
  q[qt] = s;
  qt++;
  d = vector<int>(n, -1);
  d[s] = 0;
  while (qh < qt) {
    int v = q[qh];
    qt++;
    for (int to = 0; to < n; to++)
      if (d[to] == -1 && f[v][to] < c[v][to]) {
        q[qt] = to;
        qt++;
        d[to] = d[v] + 1;
      }
  }
  return (d[t] != -1);
}

int dfs(int v, int flow) {

  if (flow == 0) { return 0; }

  if (v == t) { return flow; }

  for (int to = ptr[v]; to < n; to++) {
    if (d[to] != d[v] + 1) { continue; }
    int push = dfs(to, min(flow, c[v][to] - f[v][to]));
    if (push) {
      f[v][to] += push;
      f[to][v] -= push;
      return push;
    }
    ptr[v]++;
  }
  return 0;
}

int main() {
  fin >> n >> s >> t;
  c = vector<vector<int> >(n, vector<int>(n, 0));
  f = vector<vector<int> >(n, vector<int>(n, 0));
  d = vector<int>(n, -1);
  ptr = vector<int>(n, 0);
  q = vector<int>(n, 0);

  while (!fin.eof()) {
    int x, y;
    fin >> x >> y;
    fin >> c[x][y];
  }

  int flow = 0;
  while (true) {
    if (!bfs()) {
      break;
    }
    ptr = vector<int>(n, 0);
    while (int push = dfs(s, INF)) {
      flow += push;
    }

  }
  fout << flow;
  return 0;
}
