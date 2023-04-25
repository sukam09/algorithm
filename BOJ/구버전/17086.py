from collections import deque

N, M = map(int, input().split())
watertank = [list(map(int, input().split())) for _ in range(N)]
q = deque([(i, j) for i in range(N) for j in range(M) if watertank[i][j]])
dist = [[0] * M for _ in range(N)]
while q:
    x, y = q.popleft()
    cur = dist[x][y]
    next = (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    for nx, ny in next:
        if 0 <= nx < N and 0 <= ny < M:
            if not dist[nx][ny] and not watertank[nx][ny]:
                q.append((nx, ny))
                dist[nx][ny] = cur + 1
print(max(map(max, dist)))