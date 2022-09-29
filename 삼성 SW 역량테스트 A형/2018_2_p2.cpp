#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;
#define X first
#define Y second

int n;
int board[25][25];
int dx[4] = { -1, 0, 0, 1 }; // 상, 좌, 우, 하
int dy[4] = { 0, -1, 1, 0 };
int ans = 0;
int x, y; // 전투로봇의 현재 위치
int lv = 2;
int exp_ = 0;
int dist[25][25];

bool OOB(int x, int y) {
	return x < 0 || x >= n || y < 0 || y >= n;
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	for (int i = 0;i < n; i++) {
		for (int j = 0; j < n;j++) {
			cin >> board[i][j];
			if (board[i][j] == 9) {
				x = i; y = j;
				board[i][j] = 0;
			}
		}
	}
	while (true) {
		queue<pii> q;
		for (int i = 0;i < n; i++)
			fill(dist[i], dist[i] + n, -1);
		dist[x][y] = 0;
		q.push({ x, y });
		vector<ti3> target;
		while (!q.empty()) {
			auto cur = q.front(); q.pop();
			if (board[cur.X][cur.Y] >= 1 && board[cur.X][cur.Y] <= 6 && board[cur.X][cur.Y] < lv)
					target.push_back({ dist[cur.X][cur.Y], cur.X, cur.Y });
			for (int dir = 0; dir < 4; dir++) {
				int nx = cur.X + dx[dir];
				int ny = cur.Y + dy[dir];
				if (OOB(nx, ny)) continue;
				if (dist[nx][ny] != -1) continue; // 방문했으면 pass
				if (board[nx][ny] > lv) continue; // 지나갈 수 없음
				dist[nx][ny] = dist[cur.X][cur.Y] + 1;
				q.push({ nx, ny });
			}
		}
		if (target.empty()) {
			cout << ans;
			return 0;
		}
		sort(target.begin(), target.end());
		int dd, xx, yy;
		tie(dd, xx, yy) = target[0];
		// 전투 로봇 이동
		ans += dd;
		x = xx;
		y = yy;
		board[x][y] = 0;
		exp_++;
		if (exp_ == lv) {
			lv++;
			exp_ = 0;
		}
	}
}