#include <bits/stdc++.h>
using namespace std;

int n;
int board[25][25];
int brute[25];
int ans = 0x7f7f7f7f;

void solve() {
	int a = 0, b = 0;
	vector<int> v1;
	vector<int> v2;
	for (int i = 0;i < n; i++) {
		if (brute[i] == 0) v1.push_back(i);
		else v2.push_back(i);
	}
	for (auto x : v1)
		for (auto y : v1)
			a += board[x][y];
	for (auto x : v2)
		for (auto y : v2)
			b += board[x][y];
	int mn = abs(a - b);
	ans = min(ans, mn);
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0;j < n;j++)
			cin >> board[i][j];
	fill(brute + n / 2, brute + n, 1);
	do {
		solve();
	} while (next_permutation(brute, brute + n));
	cout << ans;
}