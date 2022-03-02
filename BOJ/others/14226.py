from collections import deque

def solution():
    while q:
        cur = q.popleft()
        i, c = cur[0], cur[1]
        now = times[i][c]
        for ni, nc in (i, i), (i + c, c), (i - 1, c):
            if ni == S:
                return now + 1
            if 0 <= ni <= 1000 and 0 <= nc <= 1000 and not times[ni][nc]:
                if (ni, nc) == (i + c, c):
                    if c:
                        q.append((ni, nc))
                        times[ni][nc] = now + 1
                else:
                    q.append((ni, nc))
                    times[ni][nc] = now + 1

S = int(input())
times = [[0] * 1001 for _ in range(1001)]
q = deque([(1, 0)])
print(solution())