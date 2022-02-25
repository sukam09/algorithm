#include <bits/stdc++.h>
using namespace std;

int n, a, b;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("/home/sukam09/algorithm/input.txt", "r", stdin);
    
    cin >> n;
    while (n--) {
        cin >> a >> b;
        cout << gcd(a, b) * (a / gcd(a, b)) * (b / gcd(a, b)) << '\n';
    }   
}