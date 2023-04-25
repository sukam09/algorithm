#include <bits/stdc++.h>
using namespace std;

bool broken[10];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  while (m--) {
    int x;
    cin >> x;
    broken[x] = true;
  }
  int ans = abs(n - 100);
  for (int i = 0; i < 1000000; i++) {
    string num = to_string(i);
    bool chk = true;
    for (auto c : num) {
      int d = c - '0';
      if (broken[d]) {
        chk = false;
        break;
      } 
    }
    if (!chk) continue;
    ans = min(ans, (int)num.size() + abs(n - i));
  }
  cout << ans;
}