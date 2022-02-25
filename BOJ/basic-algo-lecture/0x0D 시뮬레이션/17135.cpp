#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int> ti3;
#define pb push_back

int n, m, d;
int arr[20][20];
int a[20][20];
int enemy;
vector<ti3> epos;

int dist(int i, int j, int arow, int acol) {
    return abs(i - arow) + abs(j - acol);
}

void shoot(int arow, int x, int y, int z) {
    epos.clear();
    for (int acol : {x, y, z}) {
        priority_queue<ti3, vector<ti3>, greater<ti3>> pq;
        for (int i = 0; i < arow; i++) {
            for (int j = 0; j < m; j++)
                if (a[i][j] && dist(i, j, arow, acol) <= d)
                    pq.push({dist(i, j, arow, acol), j, i});
        }
        if (!pq.empty()) {
            int dd, yy, xx;
            tie(dd, yy, xx) = pq.top();
            epos.pb({xx, yy, dd});
        }
    }
}

int solve(int x, int y, int z) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = arr[i][j];

    int arow = n;
    int ret = 0;
    int e = enemy;
    
    while (e) {
        shoot(arow, x, y, z);
        for (auto cur : epos) {
            int xx, yy, dd;
            tie(xx, yy, dd) = cur;
            if (a[xx][yy]) {
                a[xx][yy] = 0;
                e--; ret++;
            }
        }
        for (int col = 0; col < m; col++)
            if (a[arow - 1][col]) a[arow - 1][col] = 0, e--;
        arow--;
    }
    return ret;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("/home/sukam09/algorithm/input.txt", "r", stdin);
    
    cin >> n >> m >> d;
    for (int i = 0; i < n ; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            if (arr[i][j]) enemy++;
        }
    }
    
    int ans = 0;
    for (int i = 0; i < m; i++)
        for (int j = i + 1; j < m; j++)
            for (int k = j + 1; k < m; k++)
                ans = max(ans, solve(i, j, k));
    
    cout << ans;
}