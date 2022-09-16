from sys import stdin
from collections import deque
input = stdin.readline

def traverse():
    vis = [[0] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if vis[i][j] or not board[i][j]:
                continue
            idx += 1
            q = deque([(i, j)])
            vis[i][j] = 1
            while q:
                x, y = q.popleft()
                island[x][y] = idx
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if oob(nx, ny) or not board[nx][ny] or vis[nx][ny]:
                        continue
                    vis[nx][ny] = 1
                    q.append((nx, ny))

def bfs(i, j):
    q = deque([(i, j, 0)])
    vis = [[0] * n for _ in range(n)]
    vis[i][j] = 1
    init = island[i][j]
    while q:
        x, y, dist = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if oob(nx, ny) or vis[nx][ny]:
                continue
            if board[nx][ny]:
                if island[nx][ny] != init:
                    return dist
                else:
                    continue
            vis[nx][ny] = 1
            q.append((nx, ny, dist + 1))
    return float('inf')

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= n
ans = float('inf')
island = [[0] * n for _ in range(n)]
traverse()

for i in range(n):
    for j in range(n):
        if not board[i][j]:
            continue
        ans = min(ans, bfs(i, j))
print(ans)