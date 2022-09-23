#include <bits/stdc++.h>
using namespace std;

int d[20][2];
int t[20];
int p[20];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++)
    cin >> t[i] >> p[i];
  for (int i = n; i >= 1; i--) {
    d[i][0] = max(d[i + 1][0], d[i + 1][1]);
    int j = i + t[i];
    d[i][1] = j <= n + 1 ? p[i] + max(d[j][0], d[j][1]) : 0;
  }
  cout << max(d[1][0], d[1][1]);
}