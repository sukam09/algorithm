/*
구현 꼬임
노란색 보드 빨간색 보드 함수 2개 각각 다르게 하여 처음부터 다시 설계할것
*/
#include <iostream>
#include <vector>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

vector<vector<int>> board1(6, vector<int>(4)); // 노란색
vector<vector<int>> board2(6, vector<int>(4)); // 빨간색
int score;
int cnt;
vector<vector<pii>> type = { {{0, 0}}, {{0, 0}, {0, 1}}, {{0, 0}, {-1, 0}}, {{0, 0}, {1, 0}}, {{0, 0}, {0, -1}} }; // 보드 방향이 다를 경우 1, 2가 서로 바뀜
// 3, 4는 빨간색 보드용

void move(int t, int x, int y, vector<vector<int>>& board) {
  while (true) {
    cout << x << '\n';
    int nx = x + 1;
    if (nx == 6) {
      for (auto& z : type[t]) {
        int yy = y + z.Y;
        board[][yy] = 1;
      }
      break;
    }
    // 아래에 블럭 있으면 그 위에 쌓음
    bool crash = false;
    for (auto& z : type[t]) {
      int yy = y + z.Y;
      if (board[nx][yy]) {
        crash = true;
        break;
      }
    }
    if (crash) {
      for (auto& z : type[t]) {
        int xx = x + z.X;
        int yy = y + z.Y;
        board[xx][yy] = 1;
      }
      break;
    }
    x = nx;
  }
  // 꽉 찼는지 확인
  int erased = 0;
  for (int i = 5; i >= 4; i--) {
    int block = 0;
    for (int j = 0;j < 4; j++)
      block += board[i][j];
    if (block == 4) erased++;
  }
  // 1 ~ 2줄 지우고 아래로 땡김
  if (erased == 1) {
    for (int j = 0;j < 4; j++) {
      board[5][j] = 0;
    }
    score++;
    for (int i = 5; i >= 1; i--) {
      for (int j = 0; j < 4; j++)
        board[i][j] = board[i - 1][j];
    }
  }
  else if (erased == 2) {
    for (int i = 5; i >= 4; i--) {
      for (int j = 0;j < 4; j++) {
        board[i][j] = 0;
      }
    }
    score += 2;
    for (int i = 5; i >= 2; i--) {
      for (int j = 0;j < 4; j++)
        board[i][j] = board[i - 2][j];
    }
  }
  // 연한 블록 처리
  int blur = 0;
  for (int i = 0;i < 2;i++) {
    for (int j = 0;j < 4; j++)
      if (board[i][j]) {
        blur++;
        break;
      }
  }
  for (int i = 5; i >= 2; i--) {
    for (int j = 0;j < 4; j++)
      board[i][j] = board[i - blur][j];
  }
}

void solve(int t, int x, int y) {
  // 노란색, 행쪽으로
  // 블럭을 쌓음
  int tmp = 3 - x; // 빨간색 보드용으로 미리 x좌표 계산
  move(t, 0, y, board1);
  // 빨간색 보드
  if (t != 0) t += 2;
  move(t, 0, tmp, board2);
  cout << "---------------------------------------------\n";
  for (int i = 0;i < 6; i++) {
    for (int j = 0; j < 4;j++)
      cout << board1[i][j] << ' ';
    cout << '\n';
  }
  cout << "---------------------------------------------\n";
  for (int i = 0;i < 6; i++) {
    for (int j = 0; j < 4;j++)
      cout << board2[i][j] << ' ';
    cout << '\n';
  }
  cout << "---------------------------------------------\n";
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int k;
  cin >> k;
  while (k--) {
    int t, x, y;
    cin >> t >> x >> y;
    solve(t - 1, x, y);
  }
  for (int i = 2;i <= 5; i++) {
    for (int j = 0;j < 4; j++) {
      cnt += board1[i][j];
      cnt += board2[i][j];
    }
  }
  cout << score << '\n' << cnt;
}