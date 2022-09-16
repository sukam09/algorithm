from sys import stdin
from collections import deque
input = stdin.readline

m, n, h = map(int, input().split())
box = []
vis = [[[0] * m for _ in range(n)] for _ in range(h)]
for _ in range(h):
    board = [list(map(int, input().split())) for _ in range(n)]
    box.append(board)
cnt = 0
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                cnt += 1
            elif box[i][j][k] == 1:
                vis[i][j][k] = 1
                q.append((i, j, k, 0))
dx = [0, 0, 1, 0, -1, 0]
dy = [0, 0, 0, 1, 0, -1]
dz = [1, -1, 0, 0, 0, 0]
oob = lambda z, x, y: z < 0 or z >= h or x < 0 or x >= n or y < 0 or y >= m
while q:
    z, x, y, ans = q.popleft()
    if box[z][x][y] == 0:
        cnt -= 1
    if cnt == 0:
        print(ans)
        break
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if oob(nz, nx, ny) or box[nz][nx][ny] != 0 or vis[nz][nx][ny]:
            continue
        vis[nz][nx][ny] = 1
        q.append((nz, nx, ny, ans + 1))
else:
    print(-1)