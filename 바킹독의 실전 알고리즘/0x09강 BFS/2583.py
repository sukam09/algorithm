from collections import deque
input = __import__('sys').stdin.readline

def draw():
    global x1, y1, x2, y2
    x1, y1 = m - y1, x1
    x2, y2 = m - y2, x2
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

def solve():
    cnt = 0
    area = []
    vis = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if vis[i][j] or board[i][j]:
                continue
            cnt += 1
            vis[i][j] = 1
            q = deque([(i, j)])
            a = 0
            while q:
                x, y = q.popleft()
                a += 1
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if oob(nx, ny) or board[nx][ny] or vis[nx][ny]:
                        continue
                    vis[nx][ny] = 1
                    q.append((nx, ny))
            area.append(a)
    print(cnt)
    print(*sorted(area))

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    draw()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= m or y < 0 or y >= n
solve()