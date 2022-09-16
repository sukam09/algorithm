#include <bits/stdc++.h>
using namespace std;
int t;
string a, b;
vector<bool> p(10000, true);

void sieve() {
    for (int i = 2; i <= 9999; i++) {
        if (!p[i]) continue;
        for (int j = i * i; j <= 9999; j += i)
            p[j] = false;
    }
}

void solve() {
    queue<string> q;
    vector<int> dist(10000, -1);
    q.push(a);
    dist[stoi(a)] = 0;
    while (!q.empty()) {
        string cur = q.front(); q.pop();
        int d = dist[stoi(cur)];
        if (cur == b) {
            cout << dist[stoi(b)] << '\n';
            return;
        }
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == cur[i]) continue;
                string nxt = cur;
                nxt[i] = j + '0';
                int n = stoi(nxt);
                if (n < 1000 || !p[n] || dist[n] != -1) continue;
                q.push(nxt);
                dist[n] = d + 1;
            }
        }
    }
    cout << "Impossible\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("/home/sukam09/algorithm/input.txt", "r", stdin);

    cin >> t;
    sieve();
    while (t--) {
        cin >> a >> b;
        solve();
    }
}