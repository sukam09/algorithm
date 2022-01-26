from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
cnt = 0
mx = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= m

for i in range(n):
    for j in range(m):
        if vis[i][j] or not board[i][j]:
            continue
        
        cnt += 1
        vis[i][j] = 1
        q = deque([(i, j)])
        area = 0
        
        while q:
            x, y = q.popleft()
            area += 1
            for d in range(4):  # 여기서 변수 i를 쓰지 않게끔 조심
                nx = x + dx[d]
                ny = y + dy[d]
                if oob(nx, ny) or not board[nx][ny] or vis[nx][ny]:
                    continue
                vis[nx][ny] = 1
                q.append((nx, ny))
        
        mx = max(mx, area)

print(cnt)
print(mx)