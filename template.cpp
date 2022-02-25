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

int main(void) {
    fastio(); fileinput();

    
}