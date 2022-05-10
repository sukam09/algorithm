#include <bits/stdc++.h>
using namespace std;

bool oob(int x, int y, int h, int w) {
    return x < 0 || x >= h || y < 0 || y >= w;
}

bool check(int x1, int y1, int x2, int y2, int h, int w, vector<string>& board) {
    return (oob(x1, y1, h, w) || board[x1][y1] == '0') && (oob(x2, y2, h, w) || board[x2][y2] == '0');
}

int solution(int h, int w, int n, vector<string> board) {
    int ans = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w - n + 1; j++) {
            bool flag = true;
            for (int k = 0; k < n; k++) {
                if (board[i][j + k] == '0') {
                    flag = false; break;
                }
            }
            if (flag && check(i, j - 1, i, j + n, h, w, board)) ans++;
        }
    }
    for (int i = 0; i < h - n + 1; i++) {
        for (int j = 0; j < w; j++) {
            bool flag = true;
            for (int k = 0; k < n; k++) {
                if (board[i + k][j] == '0') {
                    flag = false; break;
                }
            }
            if (flag && check(i - 1, j, i + n, j, h, w, board)) ans++;
        }
    }
    for (int i = 0; i < h - n + 1; i++) {
        for (int j = 0; j < w - n + 1; j++) {
            bool flag = true;
            for (int k = 0; k < n; k++) {
                if (board[i + k][j + k] == '0') {
                    flag = false; break;
                }
            }
            if (flag && check(i - 1, j - 1, i + n, j + n, h, w, board)) ans++;
        }
    }
    for (int i = 0; i < h - n + 1; i++) {
        for (int j = n - 1; j < w; j++) {
            bool flag = true;
            for (int k = 0; k < n; k++) {
                if (board[i + k][j - k] == '0') {
                    flag = false; break;
                }
            }
            if (flag && check(i - 1, j + 1, i + n, j - n, h, w, board)) ans++;
        }
    }
    return ans;
}