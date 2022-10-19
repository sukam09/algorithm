#include <bits/stdc++.h>
using namespace std;

int n, k;
deque<int> board[100];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

bool chk() {
  int mx = *max_element(board[99].begin(), board[99].end());
  int mn = *min_element(board[99].begin(), board[99].end());
  return mx - mn <= k;
}

void solve() {
  // 1
  int mn = *min_element(board[99].begin(), board[99].end());
  for (int i = 0;i < (int)board[99].size(); i++)
    if (board[99][i] == mn) board[99][i]++;
  // 2
  int top = 99;
  while (true) {
    if (99 - top + 1 > (int)board[99].size() - (int)board[98].size()) break;
    if (top == 99) {
      int x = board[99].front(); board[99].pop_front();
      board[98].push_front(x);
      top--;
    }
    else {
      int sz = (int)board[98].size();
      queue<int> q;
      for (int j = sz - 1; j >= 0; j--) {
        for (int i = 99; i >= top; i--) {
          q.push(board[i][j]);
        }
      }
      int cnt = (int)board[98].size();
      while (cnt--) board[99].pop_front();
      int height = (int)board[98].size() + 1;
      top = 99 - height + 1;
      for (int i = 98; i >= top; i--) {
        board[i].clear();
        for (int j = 0;j < 99 - top + 1; j++) {
          auto cur = q.front(); q.pop();
          board[i].push_back(cur);
        }
      }
    }
    for (int i = 97; i < 100; i++) {
      for (auto x : board[i]) cout << x << ' ';
      cout << '\n';
    }
  }

  // 3
  vector<vector<int>> nxt(100, vector<int>(100));
  for (int i = top;i <= 99; i++) {
    for (int j = 0; j < (int)board[i].size(); j++) {
      for (int dir = 0; dir < 4; dir++) {
        int nx = i + dx[dir];
        int ny = j + dy[dir];
        if (OOB(nx, ny)) continue;
        int d = abs(board[i][j] - board[nx][ny]) / 5;
        if (board[i][j] > board[nx][ny]) {
          nxt[i][j] -= d;
          nxt[nx][ny] += d;
        }
        else if (board[i][j] < board[nx][ny]) {
          nxt[i][j] += d;
          nxt[nx][ny] -= d;
        }
      }
    }
  }
  for (int i = top; i <= 99; i++) {
    for (int j = 0;j < (int)board[i].size(); j++) {
      board[i][j] += nxt[i][j];
    }
  }
  // 도우 일자로 펴기
  top = 99;
  board[99].clear();
  // 4
  // 5
  queue<int> ret;
  for (int j = 0;j < (int)board[99].size(); j++) {
    for (int i = 99; i >= top; i--) {
      ret.push(board[i][j]);
    }
  }
  board[99].clear();
  while (!ret.empty()) {
    auto cur = ret.front(); ret.pop();
    board[99].push_back(cur);
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> k;
  for (int i = 0;i < n;i++) {
    int x;
    cin >> x;
    board[99].push_back(x);
  }
  int ans = 0;
  while (true) {
    if (chk()) {
      cout << ans;
      return 0;
    }
    ans++;
    solve();
    break;
  }
}