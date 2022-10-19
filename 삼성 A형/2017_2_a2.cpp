#include <bits/stdc++.h>
using namespace std;

int n, l;
int board[105][105];

bool OOB(int x) {
	return x < 0 || x >= n;
}

int brute(int cur, int dir) {
	vector<int> h(n); // 보도블럭 높이
	vector<int> chk(n); // 경사로가 설치되었는가? (1: 올라가는 경사로, 2: 내려가는 경사로)
	if (dir == 0) {
		for (int j = 0;j < n; j++)
			h[j] = board[cur][j];
	}
	else {
		for (int i = 0;i < n; i++)
			h[i] = board[i][cur];
	}
	for (int j = 0;j < n - 1; j++) {
		// 1. 높이가 모두 같은가?
		int idx = -1; // 경사로를 설치할 위치
		int k = -1; // 경사로의 종류
		if (h[j] == h[j + 1]) continue;
		if (h[j] < h[j + 1]) {
			if (h[j + 1] - h[j] > 1) return 0; // 높이가 2 이상 차이나면 안됨
			if (chk[j] == 1) continue; // 올라가는 경사로일때만 통과
			idx = j;
			k = 1;
		}
		else {
			if (h[j] - h[j + 1] > 1) return 0;
			if (chk[j + 1] == 2) continue; // 내려가는 경사로일때만 통과
			idx = j + 1;
			k = 2;
		}
		// 2. 경사로 설치
		// 올라가는 경사로
		if (k == 1) {
			if (OOB(idx - l + 1)) return 0; // 경사로의 길이만큼 낮은 칸의 보도블럭이 연속하지 않음
			for (int y = idx;y > idx - l; y--) {
				if (chk[y] != 0) return 0; // 이미 경사로가 있으면 설치 불가능
				if (y == idx - l + 1) {
					chk[y] = k;
					break;
				} // 마지막이면 옆이랑 높이 체크 안해도됨
				if (h[y] != h[y - 1]) return 0; // 경사로를 설치할 낮은 블럭의 높이가 같지 않음
				chk[y] = k;
			}
		}
		// 내려가는 경사로
		else {
			if (OOB(idx + l - 1)) return 0; // 경사로의 길이만큼 낮은 칸의 보도블럭이 연속하지 않음
			for (int y = idx; y < idx + l; y++) {
				if (chk[y] != 0) return 0; // 이미 경사로가 있으면 설치 불가능
				if (y == idx + l - 1) {
					chk[y] = k;
					break; // 마지막이면 옆이랑 높이 체크 안해도됨
				}
				if (h[y] != h[y + 1]) return 0; // 경사로를 설치할 낮은 블럭의 높이가 같지 않음
				chk[y] = k;
			}
		}
	}
	// 블럭의 높이가 모두 같음
	return 1;
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> l;
	for (int i = 0; i < n; i++)
		for (int j = 0;j < n;j++)
			cin >> board[i][j];
	int ans = 0;
	// dir: 0은 가로, 1은 세로
	for (int i = 0;i < n; i++) {
		int ret = brute(i, 0);
		ans += ret;
	}
	for (int i = 0;i < n; i++) {
		int ret = brute(i, 1);
		ans += ret;
	}
	cout << ans;
}