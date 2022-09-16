from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
q = deque([(0, 0, 0)])
dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
dist[0][0][0] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= m
while q:
    x, y, b = q.popleft()
    nd = dist[x][y][b] + 1
    if (x, y) == (n - 1, m - 1):
        print(dist[n - 1][m - 1][b])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if oob(nx, ny):
            continue
        if not board[nx][ny] and dist[nx][ny][b] == -1:
            dist[nx][ny][b] = nd
            q.append((nx, ny, b))
        if not b and board[nx][ny] and dist[nx][ny][1] == -1:
            dist[nx][ny][1] = nd
            q.append((nx, ny, 1))
else:
    print(-1)