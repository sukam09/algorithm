from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
oob = lambda x: x < 0 or x > 100000
q = deque([(n, 0)])
vis = [0] * 100001
vis[n] = 1
while q:
    x, ans = q.popleft()
    if x == k:
        print(ans)
        break
    for nx in x - 1, x + 1, 2 * x:
        if oob(nx) or vis[nx]:
            continue
        vis[nx] = 1
        q.append((nx, ans + 1))