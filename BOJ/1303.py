from collections import deque

N, M = map(int, input().split())
soldier = [input() for _ in range(M)]
vis = [[0] * N for _ in range(M)]
ally = 0
enemy = 0
for i in range(M):
    for j in range(N):
        if vis[i][j]:
            continue
        team = soldier[i][j]
        q = deque([(i, j)])
        vis[i][j] = 1
        cnt = 1
        while q:
            x, y = q.popleft()
            for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= nx < M and 0 <= ny < N and soldier[nx][ny] == team and not vis[nx][ny]:
                    q.append((nx, ny))
                    vis[nx][ny] = 1
                    cnt += 1
        if team == 'W':
            ally += cnt ** 2
        else:
            enemy += cnt ** 2
print(ally, enemy)