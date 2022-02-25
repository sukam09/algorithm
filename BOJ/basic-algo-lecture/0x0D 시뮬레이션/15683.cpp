#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef tuple<int, int, int> ti3;
#define X first
#define Y second
#define pb push_back

int n, m;
int a[13][13];
int sz;
int ans = 100;
vector<ti3> v;

int chk() {
    int ret = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (a[i][j] == 0) ret++;
    return ret;
}

void init(vector<pii>& tmp) {
    for (auto cur : tmp) a[cur.X][cur.Y] = 0;
}

void f(int x, int y, int dir, vector<pii>& tmp) {
    if (dir == 0) {
        for (int i = y + 1; i < m; i++) {
            if (a[x][i] == 6) break;
            if (a[x][i] != 0) continue;
            a[x][i] = 7;
            tmp.push_back({x, i});
        }
    }
    else if (dir == 1) {
        for (int i = y - 1; i >= 0; i--) {
            if (a[x][i] == 6) break;
            if (a[x][i] != 0) continue;
            a[x][i] = 7;
            tmp.push_back({x, i});
        }
    }
    else if (dir == 2) {
        for (int i = x - 1; i >= 0; i--) {
            if (a[i][y] == 6) break;
            if (a[i][y] != 0) continue;
            a[i][y] = 7;
            tmp.push_back({i, y});
        }
    }
    else {
        for (int i = x + 1; i < n; i++) {
            if (a[i][y] == 6) break;
            if (a[i][y] != 0) continue;
            a[i][y] = 7;
            tmp.push_back({i, y});
        }
    }
}

void solve(int cnt) {
    if (cnt == sz) {
        ans = min(ans, chk());
        return;
    }
    
    int z, x, y;
    tie(z, x, y) = v[cnt];
    
    if (z == 1) {
        for (int i = 0; i < 4; i++) {
            vector<pii> tmp;
            f(x, y, i, tmp);
            solve(cnt + 1);
            init(tmp);
        }
    }
    else if (z == 2) {
        for (int i = 0; i < 2; i++) {
            vector<pii> tmp;
            f(x, y, 2 * i, tmp);
            f(x, y, 2 * i + 1, tmp);
            solve(cnt + 1);
            init(tmp);
        }
    }
    else if (z == 3) {
        pii d[] = {{0, 2}, {0, 3}, {1, 3}, {1, 2}};
        for (int i = 0; i < 4; i++) {
            vector<pii> tmp;
            f(x, y, d[i].X, tmp);
            f(x, y, d[i].Y, tmp);
            solve(cnt + 1);
            init(tmp);
        }
    }
    else if (z == 4) {
        for (int i = 0; i < 4; i++) {
            vector<pii> tmp;
            for (int j = 0; j < 4; j++) {
                if (i == j) continue;
                f(x, y, j, tmp);
            }
            solve(cnt + 1);
            init(tmp);
        }
    }
    else {
        vector<pii> tmp;
        for (int i = 0; i < 4; i++)
            f(x, y, i, tmp);
        solve(cnt + 1);
        init(tmp);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
            if (a[i][j] >= 1 && a[i][j] <= 5) v.pb({a[i][j], i, j});
        }
    }

    sz = v.size();
    solve(0);
    cout << ans;
}