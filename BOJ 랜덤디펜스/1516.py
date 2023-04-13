import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
costs = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    costs[i] = info[0]
    for j in range(1, len(info) - 1):
        adj[info[j]].append(i)
        deg[i] += 1
q = deque()
d = [0] * (n + 1)
for i in range(1, n + 1):
    if deg[i] == 0:
        q.append(i)
        d[i] = costs[i]
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        deg[nxt] -= 1
        d[nxt] = max(d[nxt], d[cur])
        if deg[nxt] == 0:
            q.append(nxt)
            d[nxt] += costs[nxt]
for i in range(1, n + 1):
    print(d[i])