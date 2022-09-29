#include <bits/stdc++.h>
using namespace std;

int n, m, h;
int board[35][15]; // 1은 오른쪽, 2는 왼쪽으로 이동
int dir[3] = { 0, 1, -1 };

// 버그가 안일어나는가?
bool chk() {
    for (int j = 0;j < n; j++) {
        int pos = j; // 데이터 위치
        for (int i = 0;i < h;i++) {
            pos += dir[board[i][pos]];
        }
        if (pos != j) return 0; // 버그
    }
    return 1;
}

int main(void) {
    cin >> n >> m >> h;
    while (m--) {
        int a, b;
        cin >> a >> b;
        a--; b--; // 0-index로 전처리
        board[a][b] = 1;
        board[a][b + 1] = 2;
    }
    int num = h * n; // 격자 크기
    // 0개
    if (chk()) {
        cout << 0;
        return 0;
    }
    // 1개
    for (int i = 0;i < num; i++) {
        // 한번에 점을 2개씩 처리
        int y = i % n;
        int x = i / n;
        // 맨 오른쪽 점은 처리 안함
        if (y == n - 1) continue;
        // 사다리가 한쪽이라도 걸려있으면 설치x
        if (board[x][y] != 0 || board[x][y + 1] != 0) continue;
        board[x][y] = 1; board[x][y + 1] = 2;   
        if (chk()) {
            cout << 1;
            return 0;
        }
        board[x][y] = 0; board[x][y + 1] = 0;
    }
    // 2개
    for (int i = 0;i < num;i++) {
        for (int j = i + 2; j < num; j++) {
            // 사다리를 이어서 설치할 수 없음
            if (j == i + 1) continue;
            int y1 = i % n, x1 = i / n;
            int y2 = j % n, x2 = j / n;
            if (y1 == n - 1 || y2 == n - 1) continue;
            if (board[x1][y1] != 0 || board[x1][y1 + 1] != 0 || board[x2][y2] != 0 || board[x2][y2 + 1] != 0) continue;
            board[x1][y1] = 1; board[x1][y1 + 1] = 2;
            board[x2][y2] = 1; board[x2][y2 + 1] = 2;
            if (chk()) {
                cout << 2;
                return 0;
            }
            board[x1][y1] = 0; board[x1][y1 + 1] = 0;
            board[x2][y2] = 0; board[x2][y2 + 1] = 0;
        }
    }
    // 3개
    for (int i = 0; i < num; i++) {
        for (int j = i + 2; j < num; j++) {
            for (int k = j + 2; k < num; k++) {
                if (j == i + 1 || k == j + 1) continue;
                int y1 = i % n, x1 = i / n;
                int y2 = j % n, x2 = j / n;
                int y3 = k % n, x3 = k / n;
                if (y1 == n - 1 || y2 == n - 1 || y3 == n - 1) continue;
                if (board[x1][y1] != 0 || board[x1][y1 + 1] != 0 || board[x2][y2] != 0 || board[x2][y2 + 1] != 0 || board[x3][y3] != 0 || board[x3][y3 + 1] != 0) continue;
                board[x1][y1] = 1; board[x1][y1 + 1] = 2;
                board[x2][y2] = 1; board[x2][y2 + 1] = 2;
                board[x3][y3] = 1; board[x3][y3 + 1] = 2;
                if (chk()) {
                    cout << 3;
                    return 0;
                }
                board[x1][y1] = 0; board[x1][y1 + 1] = 0;
                board[x2][y2] = 0; board[x2][y2 + 1] = 0;
                board[x3][y3] = 0; board[x3][y3 + 1] = 0;
            }
        }
    }
    // 불가능
    cout << -1;
}