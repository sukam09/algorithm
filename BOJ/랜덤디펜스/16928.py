import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
mov = [0] * 101
for _ in range(n):
    x, y = map(int, input().split())
    mov[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    mov[u] = v
vis = [-1] * 101
vis[1] = 0
q = deque([1])
q.append(1)
while q:
    x = q.popleft()
    if mov[x] != 0:
        mx = mov[x]
        vis[mx] = vis[x]
        x = mx
    if x == 100:
        print(vis[x])
        sys.exit(0)
    for i in range(1, 7):
        nx = x + i
        if nx > 100: continue
        if vis[nx] != -1: continue
        vis[nx] = vis[x] + 1
        q.append(nx)
