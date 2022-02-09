#include <bits/stdc++.h>
using namespace std;

int board[1005][1005];
int d[1005][1005];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) board[i][j] = s[j] - '0';
    }

    int ans = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (i == 0 || j == 0) d[i][j] = board[i][j];
            else if (board[i][j]) d[i][j] = min(d[i - 1][j - 1], min(d[i - 1][j], d[i][j - 1])) + 1;
            ans = max(ans, d[i][j]);
        }
    cout << ans * ans;
}