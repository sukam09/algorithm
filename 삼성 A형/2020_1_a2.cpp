/*
board, tmp 변수 2개 쓰고 status 배열 사용 안하고 board만으로 다시 풀어보기
*/

#include <iostream>
#include <tuple>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

pii board[4][4]; // 0은 술래, -1은 빈칸
pii status[17]; // 도둑말의 위치, 없는 도둑말일 경우 (-1, -1)
int dx[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[8] = {0, -1, -1, -1, 0, 1, 1, 1};
int ans;

bool OOB(int x, int y) {
  return x < 0 || x >= 4 || y < 0 || y >= 4;
}

// 도둑말 이동
void run() {
  for (int i = 1; i <= 16; i++) {
    int x, y;
    tie(x, y) = status[i];
    if (x == -1) continue; // 존재하지 않는 도둑말
    int d = board[x][y].Y;
    for (int j = 0;j < 8;j++) {
      int dir = (d + j) % 8;
      int nx = x + dx[dir];
      int ny = y + dy[dir];
      if (OOB(nx, ny)) continue;
      int target = board[nx][ny].X;
      if (target == 0) continue; // 술래 말이 있는 곳으로는 이동 불가
      if (target > 0) {
        swap(board[x][y], board[nx][ny]);
        board[nx][ny].Y = dir; // 바뀐 방향으로 적용
        swap(status[i], status[target]);
      }
      else {
        board[nx][ny] = { i, dir };
        board[x][y] = { -1, -1 };
        status[i] = { nx, ny };
      }
    }
  }
}

void solve(int x, int y, int dir, int tot) {
  //status[board[x][y].X] = { -1, -1 }; // 도둑말 검거
  //int nd = board[x][y].Y;
  //board[x][y] = { 0, nd };
  run();
  cout << x << ' ' << y << ' ' << dir << ' ' << tot << ' ' << "----------------------------------------------------------------\n";
  for (int i = 0;i < 4; i++) {
    for (int j = 0;j < 4;j++)
      cout << board[i][j].X << ',' << board[i][j].Y << ' ';
    cout << '\n';
  }
  for (int i = 1;i <= 16; i++) cout << status[i].X << ',' << status[i].Y << ' '; cout << '\n';
  cout << "----------------------------------------------------------------\n";
  bool chk = false; // 도둑말을 발견했는가?
  while (true) {
    int nx = x + dx[dir];
    int ny = y + dy[dir];
    if (OOB(nx, ny)) break;
    if (board[nx][ny].X == -1) continue; // 도둑말이 없으면 못감
    chk = true;
    // 술래 이동
    pii tmp = board[nx][ny]; // 도둑말을 잡기 전 원래 상태
    int nd = board[nx][ny].Y;
    status[board[nx][ny].X] = { -1, -1 };
    board[nx][ny] = { 0, nd };
    board[x][y] = { -1, -1 };
    solve(nx, ny, nd, tot + board[nx][ny].X);
    board[x][y] = { 0, dir };
    board[nx][ny] = tmp;
    status[tmp.X] = { nx, ny };
    x = nx; y = ny;
  }
  if (!chk) ans = max(ans, tot);
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  for (int i = 0;i < 4; i++) {
    for (int j = 0;j < 4; j++) {
      int p, d;
      cin >> p >> d;
      board[i][j] = { p, d - 1 }; // d to 0-index
      status[p] = { i, j };
    }
  }
  int st = board[0][0].X;
  int sd = board[0][0].Y;
  cout << "----------------------------------------------------------------\n";
  for (int i = 0;i < 4; i++) {
    for (int j = 0;j < 4;j++)
      cout << board[i][j].X << ',' << board[i][j].Y << ' ';
    cout << '\n';
  }
  for (int i = 1;i <= 16; i++) cout << status[i].X << ',' << status[i].Y << ' '; cout << '\n';
  cout << "----------------------------------------------------------------\n";
  solve(0, 0, sd, st);
  cout << ans;
}