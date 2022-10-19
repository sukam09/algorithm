#include <bits/stdc++.h>
using namespace std;
using ti3 = tuple<int, int, int>; // 크기, 속도, 방향

int n, m;
ti3 board1[105][105];
vector<ti3> board2[105][105]; // 곰팡이의 이동을 나타내는 보드
int ans = 0;
// 위, 아래, 오른쪽, 왼쪽
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };

bool OOB(int x, int y) {
	return x < 0 || x >= n || y < 0 || y >= m;
}

int rev(int d) {
	if (d == 0) return 1;
	else if (d == 1) return 0;
	else if (d == 2) return 3;
	else return 2;
}

ti3 move(int x, int y, int s, int d) {
	while (s--) {
		int nx = x + dx[d];
		int ny = y + dy[d];
		if (OOB(nx, ny)) {
			d = rev(d);
			x += dx[d];
			y += dy[d];
		}
		else {
			x = nx;
			y = ny;
		}
	}
	return { x, y, d };
}

void solve(int cur) {
	for (int i = 0;i < n; i++)
		for (int j = 0;j < m; j++)
			board2[i][j].clear();
	
	// 채취
	for (int i = 0;i < n; i++) {
		int b, s, d;
		tie(b, s, d) = board1[i][cur];
		if (b == 0) continue;
		ans += b;
		board1[i][cur] = { 0, 0, 0 };
		int x, y, z;
		tie(x, y, z) = board1[i][cur];
		break;
	}
	
	// 이동
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int b, s, d;
			tie(b, s, d) = board1[i][j];
			if (b == 0) continue;
			int nx, ny, nd;
			tie(nx, ny, nd) = move(i, j, s, d);
			board2[nx][ny].push_back({ b, s, nd });
		}
	}

	// 잡아먹음
	for (int i = 0;i < n; i++) {
		for (int j = 0;j < m; j++) {
			// 정렬해서 맨 앞칸에 크기가 가장 큰 곰팡이만 남김
			if (board2[i][j].empty()) continue;
			sort(board2[i][j].begin(), board2[i][j].end(), greater<ti3>());
		}
	}
	for (int i = 0;i < n; i++) {
		for (int j = 0;j < m;j++) {
			if (board2[i][j].empty()) board1[i][j] = { 0, 0, 0 };
			else board1[i][j] = board2[i][j][0];
		}
	}
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int k;
	cin >> n >> m >> k;
	while (k--) {
		int x, y, s, d, b;
		cin >> x >> y >> s >> d >> b;
		board1[x - 1][y - 1] = { b, s, d - 1 }; // 0-index
	}
	for (int j = 0;j < m;j++)
		solve(j);
	cout << ans;
}