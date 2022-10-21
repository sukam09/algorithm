#include <bits/stdc++.h>
using namespace std;

int a[1005];
int b[1005]; // 가장 긴 증가수열 길이(앞에서부터)
int c[1005]; // 가장 긴 감소수열 길이(뒤에서부터)

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> a[i];
  fill(b, b + n, 1);
  fill(c, c + n, 1);
  for (int i = 0;i < n;i++)
    for (int j =0;j < i;j++)
      if (a[j] < a[i])
        b[i] = max(b[i], b[j] + 1);
  for (int i = n - 1; i >= 0; i--)
    for (int j = n - 1; j > i; j--)
      if (a[j] < a[i])
        c[i] = max(c[i], c[j] + 1);
  int ans = 0;
  for (int i = 0;i < n;i++) {
    int mx1 = 0, mx2 = 0;
    for (int j = 0;j < i; j++) {
      if (a[j] < a[i]) mx1 = max(mx1, b[j]);
    }
    for (int j = i + 1;j < n; j++) {
      if (a[i] > a[j]) mx2 = max(mx2, c[j]);
    }
    int mx = mx1 + mx2 + 1;
    ans = max(ans, mx);
  }
  cout << ans;
}