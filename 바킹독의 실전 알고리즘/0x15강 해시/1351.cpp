#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int p, q;
unordered_map<ll, ll> m;

ll dfs(ll i) {
  if (m[i] > 0) return m[i];
  return m[i] = dfs(i / p) + dfs(i / q);
}

int main(void) {
  ll n;
  cin >> n >> p >> q;
  m[0] = 1;
  cout << dfs(n);
}