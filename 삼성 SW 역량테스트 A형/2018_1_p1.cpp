#include <bits/stdc++.h>
using namespace std;

int n;
int board[105][105];
// 우, 상, 좌, 하
int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};
// 사각형 방향벡터
int sx[4] = {0, 0, 1, 1};
int sy[4] = {0, 1, 0, 1};

int rev(int dir) {
	return (dir + 2) % 4;
}

void solve(int x, int y, int d, int g) {
	vector<int> route;
	for (int deg = 0; deg <= g; deg++) {
		if (deg == 0) {
			route.push_back(d);
		}
		else if (deg == 1) {
			route.push_back((d + 1) % 4);
		}
		else {
			int sz = route.size();
			// 앞에 절반은 뒤집어서 붙여주고 뒤에는 그대로 붙임
			for (int i = 0; i < sz; i++) {
				if (i < sz / 2) {
					int rr = rev(route[i]);
					route.push_back(rr);
				}
				else {
					route.push_back(route[i]);
				}
			}
		}
	}
	board[x][y] = 1; // 시작점
	for (auto& r : route) {
		x += dx[r];
		y += dy[r];
		board[x][y] = 1;
	}
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	while (n--) {
		int x, y, d, g;
		cin >> x >> y >> d >> g;
		swap(x, y);
		solve(x, y, d, g);
	}
	int ans = 0;
	for (int i = 0;i <= 99; i++) {
		for (int j = 0;j <= 99; j++) {
			int cnt = 0;
			for (int k = 0;k < 4; k++) {
				int x = i + sx[k];
				int y = j + sy[k];
				if (board[x][y] == 1) cnt++;
				else break; // 하나라도 만족하지 않으면
			}
			if (cnt == 4) ans++;
		}
	}
	cout << ans;
}