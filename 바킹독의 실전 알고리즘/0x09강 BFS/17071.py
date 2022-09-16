import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n, k = mis()
q = deque([(n, 0)])
dist = [[-1] * 2 for _ in range(500001)]
dist[n][0] = 0
oob = lambda v: v < 0 or v > 500000
while q:
    v, d = q.popleft()
    nd = d + 1
    for nv in v - 1, v + 1, v * 2:
        if oob(nv) or dist[nv][nd % 2] != -1:
            continue
        dist[nv][nd % 2] = d + 1
        q.append((nv, d + 1))
cur = k
ans = 0
while cur <= 500000:
    if dist[cur][ans % 2] <= ans:
        print(ans)
        break
    ans += 1
    cur += ans
else:
    print(-1)