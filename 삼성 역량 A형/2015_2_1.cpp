#include <bits/stdc++.h>
using namespace std;

using ll = long long;
int rest[1000005];

int main(void) {
  int n, a, b;
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> rest[i];
  cin >> a >> b;
  ll ans = 0;
  for (int i = 0; i < n; i++) {
    if (rest[i] <= a) {
      ans++;
      continue;
    }
    rest[i] -= a; // 팀장
    ans += 1 + ceil((double)rest[i] / (double)b);
  }
  cout << ans;
}