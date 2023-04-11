import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
wall = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 1:
            wall += 1
# 갈 수 있는 칸은 벽과 비활성 바이러스를 제외한 모든 칸
cnt = n ** 2 - wall - (len(virus) - m)
ans = 9999
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

for c in combinations(virus, m):
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    remain = cnt
    for x, y in c:
        # 활성 바이러스 칸
        dist[x][y] = 0
        q.append((x, y))
    while q:
        x, y = q.popleft()
        if board[x][y] == 0 or dist[x][y] == 0:
            remain -= 1
        if remain == 0:
            ans = min(ans, dist[x][y])
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if OOB(nx, ny) or dist[nx][ny] != -1 or board[nx][ny] == 1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

print(ans if ans != 9999 else -1)