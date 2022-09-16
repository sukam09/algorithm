#include <bits/stdc++.h>
using namespace std;

int a, b, c, d, e, f, g;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> a >> b >> c >> d;
    f = b * d;
    e = a * d + b * c;
    g = gcd(e, f);
    e = e / g, f = f / g;
    cout << e << ' ' << f;
}