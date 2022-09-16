#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int arr[12][12];

#define X first
#define Y second

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n;
        cin >> n;
        int connected = 0;
        int line = 0;
        vector<pair<int, int>> v;
        vector<pair<int, int>> ans;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> arr[i][j];
                if (arr[i][j] == 1) {
                    if (i == 0 || i == n - 1 || j == 0 || j == n - 1) connected++;
                    else {
                        pair<int, int> p = {i, j};
                        v.push_back(p);
                    }
                }
            }
        }
        
    }
}