from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque([(0, 0)])
    step = [[-1] * m for _ in range(n)]
    step[0][0] = 1
    
    while q:
        x, y = q.popleft()
        now = step[x][y]
        for nx, ny in (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y):
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and step[nx][ny] == -1:
                q.append((nx, ny))
                step[nx][ny] = now + 1
    
    return step[n - 1][m - 1]