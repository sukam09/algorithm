import sys
from collections import deque
input = sys.stdin.readline

def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= m

def melt():
    global cnt
    vis = [[0] * m for _ in range(n)]
    chk = [[0] * m for _ in range(n)]
    vis[0][0] = 1
    q = deque([(0, 0)])
    # 외부 공기만 bfs
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if OOB(nx, ny) or vis[nx][ny]:
                continue
            if board[nx][ny] == 0:
                vis[nx][ny] = 1
                q.append((nx, ny))
            # 치즈를 탐색할 때는 방문 체크를 하지 않음에 주의
            else:
                chk[nx][ny] += 1
    for i in range(n):
        for j in range(m):
            if chk[i][j] >= 2:
                board[i][j] = 0
                cnt -= 1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j]:
            cnt += 1
ans = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while cnt:
    ans += 1
    melt()
print(ans)