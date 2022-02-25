#include <bits/stdc++.h>
using namespace std;

#ifdef ONLINE_JUDGE
#define fastio() ios::sync_with_stdio(0); cin.tie(0)
#define fileinput() (void)0
#define debug(x) (void)0

#else
#define fastio() (void)0
#define fileinput() freopen("/home/sukam09/algorithm/input.txt", "r", stdin)
#define debug(x) cout << "[Debug] " << #x << " = " << (x) << '\n'
#endif

int lc[30];
int rc[30];

void preorder(int v) {
    cout << char(v + 'A' - 1);
    if (lc[v]) preorder(lc[v]);
    if (rc[v]) preorder(rc[v]);
}

void inorder(int v) {
    if (lc[v]) inorder(lc[v]);
    cout << char(v + 'A' - 1);
    if (rc[v]) inorder(rc[v]);
}

void postorder(int v) {
    if (lc[v]) postorder(lc[v]);
    if (rc[v]) postorder(rc[v]);
    cout << char(v + 'A' - 1);
}

int main(void) {
    fastio(); fileinput();

    int n;
    cin >> n;
    while (n--) {
        char x, l, r;
        cin >> x >> l >> r;
        int v = x - 'A' + 1;
        if (l != '.') lc[v] = l - 'A' + 1;
        if (r != '.') rc[v] = r - 'A' + 1;
    }
    preorder(1); cout << '\n';
    inorder(1); cout << '\n';
    postorder(1);
}