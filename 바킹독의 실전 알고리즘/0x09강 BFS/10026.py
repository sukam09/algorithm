from sys import stdin
from collections import deque
input = stdin.readline

def sol1():
    vis = [[0] * n for _ in range(n)]
    ans = 0
    
    for i in range(n):
        for j in range(n):
            if vis[i][j]:
                continue
            
            vis[i][j] = 1
            que = deque([(i, j)])
            ans += 1
            
            while que:
                x, y = que.popleft()
                cur = board[x][y]
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if oob(nx, ny):
                        continue
                    if board[nx][ny] != cur or vis[nx][ny]:
                        continue
                    vis[nx][ny] = 1
                    que.append((nx, ny))
    
    return ans

def sol2():
    vis = [[0] * n for _ in range(n)]
    ans = 0
    
    for i in range(n):
        for j in range(n):
            if vis[i][j]:
                continue
            
            vis[i][j] = 1
            que = deque([(i, j)])
            ans += 1
            
            while que:
                x, y = que.popleft()
                cur = board[x][y]
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if oob(nx, ny):
                        continue
                    if cur == 'B':
                        if board[nx][ny] != cur or vis[nx][ny]:
                            continue
                    else:
                        if board[nx][ny] == 'B' or vis[nx][ny]:
                            continue
                    vis[nx][ny] = 1
                    que.append((nx, ny))
    
    return ans

n = int(input())
board = [input() for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= n
print(sol1(), sol2())