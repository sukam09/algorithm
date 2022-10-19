#include <bits/stdc++.h>
using namespace std;

int n, c;
int house[200005];

bool solve(int mid) {
  int cnt = 1;
  int pre = house[0];
  for (int i = 1;i < n; i++) {
    if (house[i] - pre >= mid) {
      cnt++;
      pre = house[i];
    }
  }
  return cnt >= c;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> c;
  for (int i =0;i < n;i++) {
    int x;
    cin >> x;
    house[i] = x;
  }
  sort(house, house + n);
  int st = 1, en = house[n - 1] - house[0];
  while (st < en) {
    int mid = (st + en + 1) / 2;
    // 거리를 늘림
    if (solve(mid)) {
      st = mid;
    } else {
      en = mid - 1;
    }
  }
  cout << st;
}