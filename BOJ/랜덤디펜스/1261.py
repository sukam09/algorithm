import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
OOB = lambda x, y: x < 0 or x >= n or y < 0 or y >= m
dist = [[float("inf")] * m for _ in range(n)]
dist[0][0] = 0
q = deque([(0, 0)])
while q:
  x, y = q.popleft()
  for dir_ in range(4):
    nx = x + dx[dir_]
    ny = y + dy[dir_]
    if OOB(nx, ny) or dist[x][y] + board[nx][ny] >= dist[nx][ny]:
      continue
    dist[nx][ny] = dist[x][y] + board[nx][ny]
    q.append((nx, ny))
print(dist[-1][-1])