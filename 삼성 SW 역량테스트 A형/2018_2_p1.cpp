#include <bits/stdc++.h>
using namespace std;

int n, m, k;
int board1[15][15]; // 마지막에 추가되는 양분
int board2[15][15]; // 현재 양분 상태
vector<int> virus[15][15];
vector<int> alive[15][15];
int dead[15][15];
int dx[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dy[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };

bool OOB(int x, int y) {
	return x < 0 || x >= n || y < 0 || y >= n;
}

void solve() {
  // alive랑 dead 초기화 및 virus sort
	for (int i = 0;i < n; i++) {
    for (int j =0;j < n; j++) {
      sort(virus[i][j].begin(), virus[i][j].end());
      alive[i][j].clear();
      dead[i][j] = 0;
    }
  }
	// 1
  for (int i =0;i < n; i++) {
    for (int j= 0;j < n; j++) {
      for (auto v : virus[i][j]) {
        if (board2[i][j] < v) {
          dead[i][j] += v / 2;
          m--;
        } else {
          board2[i][j] -= v;
          alive[i][j].push_back(v + 1);
        }
      }
    }
  }
	// 2
  for (int i = 0;i < n; i++)
    for (int j =0;j < n ;j++)
      board2[i][j] += dead[i][j];
	// 3
	for (int i = 0; i < n; i++) {
		for (int j = 0;j <  n; j++) {
			for (auto a : alive[i][j]) {
				if (a % 5 != 0) continue;
				for (int dir = 0; dir < 8; dir++) {
					int x = i + dx[dir];
					int y = j + dy[dir];
					if (OOB(x, y)) continue;
					alive[x][y].push_back(1);
					m++;
				}
			}
		}
	}
	// 4
	for (int i = 0;i < n; i++) {
		for (int j = 0;j < n; j++) {
      board2[i][j] += board1[i][j];
			virus[i][j] = alive[i][j];
    }
  }		
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m >> k;
	for (int i = 0;i < n; i++)
		for (int j = 0;j < n;j++)
			cin >> board1[i][j];
	for (int i = 0; i < n; i++)
		fill(board2[i], board2[i] + n, 5);
	for (int i = 0;i < m; i++) {
		int r, c, age;
		cin >> r >> c >> age;
		virus[r - 1][c - 1].push_back(age); // 0-index
	}
	while (k--) solve();
	cout << m;
}