from sys import stdin
from collections import deque
input = stdin.readline

def bfs1():
    for x, y in q1:
        dist[x][y] = 0
    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if oob(nx, ny) or board[nx][ny] == '#' or dist[nx][ny] != float('inf'):
                continue
            dist[nx][ny] = dist[x][y] + 1
            q1.append((nx, ny))

def bfs2():
    vis[q2[0][0]][q2[0][1]] = 1
    while q2:
        x, y, ans = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if oob(nx, ny):
                print(ans + 1)
                return
            if board[nx][ny] == '#' or vis[nx][ny] or ans + 1 >= dist[nx][ny]:
                continue
            vis[nx][ny] = 1
            q2.append((nx, ny, ans + 1))
    print("IMPOSSIBLE")
 
r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]
q1 = deque()
q2 = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            q2.append((i, j, 0))
        elif board[i][j] == 'F':
            q1.append((i, j))
dist = [[float('inf')] * c for _ in range(r)]
vis = [[0] * c for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= r or y < 0 or y >= c
bfs1()
bfs2()