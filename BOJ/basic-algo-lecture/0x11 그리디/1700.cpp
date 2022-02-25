#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};
bool OOB(int x, int y, int n, int m) {return x < 0 || x >= n || y < 0 || y >= m;}

#define X first
#define Y second
#define pb push_back

#ifdef ONLINE_JUDGE
#define fastio() ios::sync_with_stdio(0); cin.tie(0)
#define fileinput() (void)0
#define debug(x) (void)0
#define pf0l() (void)0

#else
#define fastio() (void)0
#define fileinput() freopen("/home/sukam09/algorithm/input.txt", "r", stdin)
#define debug(x) cout << #x << ": " << (x) << ' '
#define pf0l() cout << '\n'
#endif

int a[105];
bool power[105];

int main(void) {
    fastio(); fileinput();

    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= k; i++) cin >> a[i];
    int ans = 0;
    int cnt = 0;
    for (int i = 1; i <= k; i++) {
        int cur = a[i];
        if (power[cur]) continue;
        if (cnt < n) {
            power[cur] = true;
            cnt++;
        }
        else {
            vector<pii> idx;
            for (int x = 1; x <= k; x++) {
                if (!power[x]) continue;
                bool vis = false;
                for (int y = i + 1; y <= k; y++) {
                    if (a[y] == x) {
                        idx.pb({y, x});
                        vis = true;
                        break;
                    }
                }
                if (!vis) idx.pb({k + 1, x});
            }
            sort(idx.begin(), idx.end(), greater<pii>());
            int target = idx[0].Y;
            power[target] = false; ans++;
            power[cur] = true;
        }
    }
    cout << ans;
}