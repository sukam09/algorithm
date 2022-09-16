#include <bits/stdc++.h>
using namespace std;
int n;

bool prime(int n) {
    if (n == 1) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}

bool palindrome(int n) {
    string s = to_string(n);
    int sz = s.size();
    for (int i = 0; i < sz / 2; i++)
        if (s[i] != s[sz - 1 - i]) return false;
    return true;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = n; i <= 1003001; i++) {
        if (prime(i) && palindrome(i)) {
            cout << i;
            return 0;
        }
    }
}