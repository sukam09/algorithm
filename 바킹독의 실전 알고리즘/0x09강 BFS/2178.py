from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= m
dist[0][0] = 1
q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    nd = dist[x][y] + 1
    if (x, y) == (n - 1, m - 1):
        print(dist[n - 1][m - 1])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if oob(nx, ny) or not board[nx][ny] or dist[nx][ny] != -1:
            continue
        dist[nx][ny] = nd
        q.append((nx, ny))