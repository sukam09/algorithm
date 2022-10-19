import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def OOB(x, y):
  return x < 0 or x >= n or y < 0 or y >= n

def bfs(x, y):
  global chk
  vis[x][y] = True
  q = deque()
  q.append((x, y))
  s = board[x][y]
  cnt = 1
  nxt = [(x, y)]
  while q:
    cur = q.popleft()
    for d in range(4):
      nx = cur[0] + dx[d]
      ny = cur[1] + dy[d]
      if OOB(nx, ny) or vis[nx][ny]:
        continue
      if l <= abs(board[nx][ny] - board[cur[0]][cur[1]]) <= r:
        vis[nx][ny] = True
        q.append((nx, ny))
        s += board[nx][ny]
        cnt += 1
        nxt.append((nx, ny))
  if len(nxt) > 1:
    chk = True
    for x, y in nxt:
      board[x][y] = s // cnt

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while True:
  chk = False
  vis = [[False] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if vis[i][j]:
        continue
      bfs(i, j)
  if not chk:
    break
  ans += 1
print(ans)