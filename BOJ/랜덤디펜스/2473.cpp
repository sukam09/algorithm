#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
ll arr[5005];
int st, en;
vector<ll> ans, cand;
ll mn = 4000000000;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + n);

  for (int i = 0; i < n - 2; i++) {
    ll sum = 0;
    st = i + 1;
    en = n - 1;
    while (st < en) {
      sum = arr[i] + arr[st] + arr[en];
      cand = {arr[i], arr[st], arr[en]};
      ll absval = abs(sum);
      if (absval < mn) {
        mn = absval;
        ans = cand;
      }
      if (sum <= 0) {
        st++;
      } else {
        en--;
      }
    }
  }

  for (auto x : ans) cout << x << ' ';
}