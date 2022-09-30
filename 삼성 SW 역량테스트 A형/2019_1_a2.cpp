#include <bits/stdc++.h>
using namespace std;

int board[55][55];
int w = -1; // 시공의 돌풍 (w, 0), (w + 1, 0)
int n, m;
int dx[4] = {-1, 0, 0, 1}; // 상, 좌, 우, 하
int dy[4] = {0, -1, 1, 0};

bool OOB(int x, int y) {
	return x < 0 || x >= n || y < 0 || y >= m;
}

void solve() {
	// 1
	vector<vector<int>> nxt(n, vector<int>(m));
	for (int i = 0;i < n; i++) {
		for (int j = 0;j < m; j++) {
			if (board[i][j] == -1) continue;
			int dust = board[i][j] / 5;
			for (int dir = 0; dir < 4; dir++) {
				int nx = i + dx[dir];
				int ny = j + dy[dir];
				if (OOB(nx, ny)) continue;
				if (board[nx][ny] == -1) continue;
				nxt[nx][ny] += dust;
				board[i][j] -= dust;
			}
		}
	}
	for (int i = 0;i < n; i++) {
		for (int j = 0;j < m; j++) {
			board[i][j] += nxt[i][j];
		}
	}

	// 2
	vector<vector<int>> tmp(n, vector<int>(m));
	tmp[w][0] = -1; tmp[w + 1][0] = -1;
	// 시공의 폭풍에 영향을 받지 않는 칸만 미리 옮겨둠
	for (int i = 1; i <= w - 1; i++)
		for (int j = 1; j <= m - 2; j++)
			tmp[i][j] = board[i][j];
	for (int i = w + 2; i <= n - 2; i++)
		for (int j = 1; j <= m - 2; j++)
			tmp[i][j] = board[i][j];
	// 반시계 방향
	for (int j = 2;j < m; j++)
		tmp[w][j] = board[w][j - 1];
	for (int i = w - 1; i >= 0; i--)
		tmp[i][m - 1] = board[i + 1][m - 1];
	for (int j = m - 2; j >= 0; j--)
		tmp[0][j] = board[0][j + 1];
	for (int i = 1; i <= w - 1; i++)
		tmp[i][0] = board[i - 1][0];
	// 시계 방향
	for (int j = 2;j < m; j++)
		tmp[w + 1][j] = board[w + 1][j - 1];
	for (int i = w + 2; i < n; i++)
		tmp[i][m - 1] = board[i - 1][m - 1];
	for (int j = m - 2; j >= 0; j--)
		tmp[n - 1][j] = board[n - 1][j + 1];
	for (int i = n - 2; i >= w + 2; i--)
		tmp[i][0] = board[i + 1][0];
	// 다 끝나고 보드에 돌려줌
	for (int i = 0;i < n; i++) {
		for (int j = 0;j < m; j++) {
			board[i][j] = tmp[i][j];
		}
	}
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> n >> m >> t;
	for (int i = 0;i < n;i++) {
		for (int j = 0; j < m; j++) {
			cin >> board[i][j];
			if (board[i][j] == -1 && w == -1) {
				w = i;
			}
		}
	}
	while (t--) solve();
	int ans = 0;
	for (int i = 0;i < n; i++) {
		for (int j = 0;j < m; j++) {
			if (board[i][j] == -1) continue;
			ans += board[i][j];
		}
	}
	cout << ans;
}