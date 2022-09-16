from sys import stdin
from collections import deque
input = stdin.readline

def solve(k):
    vis = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if vis[i][j] or board[i][j] <= k:
                continue
            cnt += 1
            q = deque([(i, j)])
            vis[i][j] = 1
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if oob(nx, ny) or vis[nx][ny] or board[nx][ny] <= k:
                        continue
                    vis[nx][ny] = 1
                    q.append((nx, ny))
    return cnt

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= n
mx = max(max(x) for x in board)
ans = 0
for i in range(mx):
    cnt = solve(i)
    ans = max(ans, cnt)
print(ans)