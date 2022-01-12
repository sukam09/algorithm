from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1

    vis = [[0] * m for _ in range(n)]
    ans = 0
    oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= m

    for i in range(n):
        for j in range(m):
            if not board[i][j] or vis[i][j]:
                continue
            
            que = deque([(i, j)])
            vis[i][j] = 1

            while que:
                x, y = que.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if oob(nx, ny):
                        continue
                    if vis[nx][ny] or not board[nx][ny]:
                        continue
                    vis[nx][ny] = 1
                    que.append((nx, ny))
            
            ans += 1
    
    print(ans)