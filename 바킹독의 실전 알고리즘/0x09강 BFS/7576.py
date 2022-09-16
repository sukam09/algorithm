from sys import stdin
from collections import deque
input = stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque()
vis = [[0] * m for _ in range(n)]
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cnt += 1
        if board[i][j] == 1:
            q.append((i, j, 0))
            vis[i][j] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= m
while q:
    x, y, ans = q.popleft()
    if board[x][y] == 0:
        cnt -= 1
    if cnt == 0:
        print(ans)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if oob(nx, ny) or board[nx][ny] != 0 or vis[nx][ny]:
            continue
        vis[nx][ny] = 1
        q.append((nx, ny, ans + 1))
else:
    print(-1)