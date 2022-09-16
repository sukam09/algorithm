from collections import deque

N, M, K = map(int, input().split())
hall = [[0] * M for _ in range(N)]
waste = []
for _ in range(K):
    r, c = map(lambda i: int(i) - 1, input().split())
    hall[r][c] = 1
    waste.append((r, c))
vis = [[0] * M for _ in range(N)]
ans = 0
for wx, wy in waste:
    if vis[wx][wy]:
        continue
    q = deque([(wx, wy)])
    vis[wx][wy] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            if 0 <= nx < N and 0 <= ny < M and hall[nx][ny] and not vis[nx][ny]:
                q.append((nx, ny))
                cnt += 1
                vis[nx][ny] = 1
    if cnt > ans:
        ans = cnt
print(ans)