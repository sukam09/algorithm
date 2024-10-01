import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, (input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            x = i
            y = j
        elif board[i][j] == 0:
            dist[i][j] = 0

q = deque()
q.append((x, y))
dist[x][y] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= m

while q:
    cx, cy = q.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if oob(nx, ny) or board[nx][ny] == 0 or dist[nx][ny] != -1:
            continue
        dist[nx][ny] = dist[cx][cy] + 1
        q.append((nx, ny))

for i in range(n):
    print(*dist[i])