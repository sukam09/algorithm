#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int num[9] = {0, 0, 1, 7, 4, 2, 0, 8, 10}; // num[i]: i개의 성냥개비로 만들 수 있는 가장 작은 수
ll d[105];

void solve(int n) {
  string mx;
  int k;
  if (n % 2 == 0) {
    k = n / 2;
  } else {
    k = (n - 3) / 2;
    mx = "7";
  }
  while (k--) mx = mx + "1";
  cout << d[n] << ' ' << mx << '\n';
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 2; i <= 8; i++)
    d[i] = i == 6 ? 6 : num[i];
  for (int i = 9;i <= 100; i++) {
    d[i] = d[i - 2] * 10 + num[2];
    for (int j = 3;j <= 7; j++)
      d[i] = min(d[i], d[i - j] * 10 + num[j]);
  }
  while (n--) {
    int m;
    cin >> m;
    solve(m);
  }
}