#include <bits/stdc++.h>
using namespace std;

const int INF = 0x3f3f3f3f;
int d[105][105];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    fill(d[i] + 1, d[i] + n + 1, INF);
    d[i][i] = 0;
  }
  while (m--) {
    int a, b, c;
    cin >> a >> b >> c;
    d[a][b] = min(d[a][b], c);
  }
  for (int k = 1; k <= n; k++)
    for (int i = 1; i <= n; i++)
      for (int j = 1; j <= n; j++)
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++)
      cout << (d[i][j] == INF ? 0 : d[i][j]) << ' ';
    cout << '\n';
  }
}