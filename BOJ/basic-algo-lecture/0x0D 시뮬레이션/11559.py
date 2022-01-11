from sys import stdin
from collections import deque
input = stdin.readline

def search(i, j):
    if board[i][j] == '.':
        return
    
    vis = [[0] * 6 for _ in range(12)]
    vis[i][j] = 1
    q = deque([(i, j)])
    color = board[i][j]
    res = [(i, j)]

    while q:
        x, y = q.popleft()
        for nx, ny in (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y):
            if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == color and not vis[nx][ny]:
                q.append((nx, ny))
                vis[nx][ny] = 1
                res.append((nx, ny))

    if len(res) >= 4:
        for nx, ny in res:
            target[ny].add(nx)

board = [list(input()) for _ in range(12)]
init = [set() for _ in range(6)]
ans = 0

while True:
    target = [set() for _ in range(6)]

    for i in range(12):
        for j in range(6):
            search(i, j)

    if target == init:
        break

    for j in range(6):
        idx = 11
        
        for i in range(11, -1, -1):
            if i not in target[j]:
                board[idx][j] = board[i][j]
                idx -= 1
        
        for i in range(idx, -1, -1):
            board[i][j] = '.'
    
    ans += 1

print(ans)