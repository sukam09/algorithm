#include <iostream>

using namespace std;

int main() {
    int tc;
    cin >> tc;

    for (int i = 1; i <= tc; i++) {
        int a, b;
        cin >> a >> b;
        int res;
        if (a >= 10 || b >= 10) res = -1;
        else res = a * b;
        cout << "#" << i << " " << res << "\n";
    }

    return 0;
}