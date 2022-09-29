#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n, m;
int board[55][55];
vector<pii> person; // 사람 위치
vector<pii> hospital; // 병원 위치
vector<pii> remain; // 남아있는 병원
int ans = 0x7f7f7f7f;

void solve() {
	int mn = 0;
	for (auto& p : person) {
		int dist = 0x7f7f7f7f;
		for (auto& r : remain)
			dist = min(dist, abs(p.X - r.X) + abs(p.Y - r.Y));
		mn += dist;
	}
	ans = min(ans, mn);
}

int main(void) {
	cin >> n >> m;
	int num = 0; // 병원 수
	for (int i = 0;i < n; i++)
		for (int j = 0;j < n; j++) {
			cin >> board[i][j];
			if (board[i][j] == 1) person.push_back({ i, j });
			else if (board[i][j] == 2) { num++; hospital.push_back({ i, j }); }
		}
	vector<int> brute(num);
	fill(brute.begin() + m, brute.end(), 1);
	do {
		remain.clear();
		for (int i = 0;i < num; i++)
			if (brute[i] == 0)
				remain.push_back(hospital[i]);
		solve();
	} while (next_permutation(brute.begin(), brute.end()));
	cout << ans;
}