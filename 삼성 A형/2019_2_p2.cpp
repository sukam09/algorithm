#include <iostream>
using namespace std;

int nxt[35];
int special[35];
int dice[10];
int ans;
int status[4];
int score[33] = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40, 0};

void solve(int cnt, int val) {
  if (cnt == 10) {
    ans = max(ans, val);
    return;
  }
  // i는 말 번호
  for (int i = 0;i < 4; i++) {
    int step = dice[cnt];
    int cur = status[i];
    int tmp = cur; // 이동하기 전 칸
    if (cur == 32) continue; // 도착 칸
    // 파란색 칸
    if (special[cur] != 0) {
      cur = special[cur];
      step--;
    }
    while (step--) {
      cur = nxt[cur];
      if (cur == 32) break;
    }
    bool found = false;
    for (int j = 0;j < 4; j++) {
      if (status[j] == cur) {
        found = true;
        break;
      }
    }
    // 도착점이 아니고 다른 말이 있으면
    if (cur != 32 && found) continue;
    status[i] = cur;
    solve(cnt + 1, val + score[cur]);
    status[i] = tmp;
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  for (int i = 0;i < 10; i++)
    cin >> dice[i];
  for (int i = 0;i <= 18; i++)
    nxt[i] = i + 1;
  nxt[19] = 31;
  nxt[31] = 32;
  nxt[20] = 21;
  nxt[21] = 22;
  nxt[22] = 28;
  nxt[23] = 24;
  nxt[24] = 28;
  nxt[25] = 26;
  nxt[26] = 27;
  nxt[27] = 28;
  nxt[28] = 29;
  nxt[29] = 30;
  nxt[30] = 31;
  special[5] = 20;
  special[10] = 23;
  special[15] = 25;
  solve(0, 0);
  cout << ans;
}