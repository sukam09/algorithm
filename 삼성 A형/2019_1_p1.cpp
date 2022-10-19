#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int r, c, k;
int a[105][105];
int row = 3;
int col = 3;

void solve(int dir) {
  int mx = 0; // 격자의 기준으로 삼을 길이
  if (dir == 0) {
    for (int i = 0;i < row; i++) {
      vector<int> cnt(101);
      for (int j = 0;j < col; j++) {
        if (a[i][j] == 0) continue;
        cnt[a[i][j]]++;
      }
      vector<pii> v; // 빈도 수, 숫자
      for (int num = 1;num <= 100; num++) {
        if (cnt[num] == 0) continue;
        v.push_back({ cnt[num], num });
      }
      sort(v.begin(), v.end());
      int sz = v.size();
      mx = max(mx, sz * 2);
      // v의 길이가 기준보다 짧을 경우 0, 0으로 채워줌
      while (v.size() < col) v.push_back({ 0, 0 });
      for (int j = 0; j < col; j++) {
        if (j >= 50) break; // j * 2가 100이 되면 stop
        a[i][j * 2] = v[j].Y;
        a[i][j * 2 + 1] = v[j].X;
      }
    }
    // 다 끝나고 나면 격자의 길이를 기준만큼 늘려줌
    col = mx;
    if (col > 100) col = 100;
  }
  else {
    for (int j = 0;j < col; j++) {
      vector<int> cnt(101);
      for (int i = 0;i < row; i++) {
        if (a[i][j] == 0) continue;
        cnt[a[i][j]]++;
      }
      vector<pii> v;
      for (int num = 1;num <= 100; num++) {
        if (cnt[num] == 0) continue;
        v.push_back({ cnt[num], num });
      }
      sort(v.begin(), v.end());
      int sz = v.size();
      mx = max(mx, sz * 2);
      // v의 길이가 기준보다 짧을 경우 0, 0으로 채워줌
      while (v.size() < row) v.push_back({ 0, 0 });
      for (int i = 0; i < row; i++) {
        if (i >= 50) break; // i * 2가 100이 되면 stop
        a[i * 2][j] = v[i].Y;
        a[i * 2 + 1][j] = v[i].X;
      }
    }
    // 다 끝나고 나면 격자의 길이를 기준만큼 늘려줌
    row = mx;
    if (row > 100) row = 100;
  }
}

int main(void) {
  cin >> r >> c >> k;
  r--; c--; // 0-index
  for (int i = 0;i < 3; i++)
    for (int j = 0;j < 3; j++)
      cin >> a[i][j];
  for (int i = 0;i < 100; i++) {
    // 왠지 답이 0인 TC가 무조건 있을 것 같다..
    if (a[r][c] == k) {
      cout << i;
      return 0;
    }
    //cout << "--------------------------------\n";
    if (row >= col) solve(0);
    else solve(1);
    /*cout << row << ' ' << col << '\n';
    for (int i = 0;i < 10; i++) {
      for (int j = 0;j < 10;j++)
        cout << a[i][j] << ' ';
      cout << '\n';
    }
    cout << "--------------------------------\n\n";*/
  }
  cout << -1;
}