#include <bits/stdc++.h>
using namespace std;
using ti3 = tuple<int, int, int>;

int n, k;
int board1[15][15];
int dx[4] = { 0, 0, -1, 1 }; // 우, 좌, 상, 하
int dy[4] = { 1, -1, 0, 0 };
vector<int> board2[15][15]; // 보드에 놓여있는 말의 상태
ti3 obj[15];

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

int rev(int d) {
  if (d == 0) return 1;
  else if (d == 1) return 0;
  else if (d == 2) return 3;
  else return 2;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> k;
  for (int i = 0;i < n;i++)
    for (int j = 0;j < n;j++)
      cin >> board1[i][j];
  for (int i = 0;i < k; i++) {
    int x, y, d;
    cin >> x >> y >> d;
    x--; y--; d--;
    board2[x][y].push_back(i);
    obj[i] = { x, y, d };
  }
  int ans = 0;
  while (ans <= 1000) {
    ans++;
    if (ans == 2) return 0;
    // i는 말 번호
    cout << "------------------------------------------\n";
    for (int i = 0;i < k;i++) {
      int cnt = 1;
      int x, y, d;
      tie(x, y, d) = obj[i];
      int idx = -1;
      int sz = board2[x][y].size();
      for (int j = 0; j < sz; j++) {
        if (board2[x][y][j] == i) {
          idx = j;
          break;
        }
      }
      int nx = x + dx[d];
      int ny = y + dy[d];
      if (OOB(nx, ny) || board1[nx][ny] == 2) {
        // 이동하려는 말만 방향을 반대로
        d = rev(d);
        get<2>(obj[board2[x][y][idx]]) = d;
        continue;
        // nx = x + dx[d];
        // ny = y + dy[d];
        // 또 파란색이면 안움직임
        // if (OOB(nx, ny) || board1[nx][ny] == 2) continue;
        // for (int j = idx; j < sz; j++) {
        //   int z = board2[x][y][j];
        //   board2[nx][ny].push_back(z);
        //   get<0>(obj[z]) = nx;
        //   get<1>(obj[z]) = ny;
          // if (board2[nx][ny].size() >= 4) {
          //   cout << ans;
          //   return 0;
          // }
        }
        for (int j = sz - 1;j >= idx; j--) board2[x][y].pop_back();
      }
      else if (board1[nx][ny] == 0) {
        // idx 위에 있는 말들을 자기 자신을 포함해서 싹다 끌고옴
        for (int j = idx; j < sz; j++) {
          int z = board2[x][y][j];
          board2[nx][ny].push_back(z);
          get<0>(obj[z]) = nx;
          get<1>(obj[z]) = ny;
          // if (board2[nx][ny].size() >= 4) {
          //   cout << ans;
          //   return 0;
          // }
        }
        for (int j = sz - 1;j >= idx; j--) board2[x][y].pop_back();
      }
      // 빨간색
      else {
        // 순서 뒤집기
        reverse(board2[x][y].begin() + idx, board2[x][y].end());
        for (int j = idx; j < sz; j++) {
          int z = board2[x][y][j];
          board2[nx][ny].push_back(z);
          get<0>(obj[z]) = nx;
          get<1>(obj[z]) = ny;
          // if (board2[nx][ny].size() >= 4) {
          //   cout << ans;
          //   return 0;
          // }
        }
        for (int j = sz - 1;j >= idx; j--) board2[x][y].pop_back();
      }
      for (int z = 0; z < k ; z++) {
        int a, b, c;
        tie(a, b, c) = obj[z];
        cout << z << ": " << a << ',' << b << ',' << c << ' ';
      }
      cout << '\n';
    }
  }
  cout << -1;
}