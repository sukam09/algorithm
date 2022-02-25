#include <bits/stdc++.h>
using namespace std;

string s;
int cnt[2];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> s;
    char cur = '2';
    for (char c : s) {
        if (c != cur) {
            cur = c;
            cnt[c - '0']++;
        }
    }
    cout << min(cnt[0], cnt[1]);
}