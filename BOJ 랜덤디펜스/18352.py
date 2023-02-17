import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
dist = [-1] * (n + 1)
dist[x] = 0
q = deque([x])
ans = []
while q:
    cur = q.popleft()
    if dist[cur] == k:
        ans.append(cur)
    for nxt in adj[cur]:
        if dist[nxt] != -1:
            continue
        dist[nxt] = dist[cur] + 1
        q.append(nxt)
if ans:
    for x in sorted(ans):
        print(x)
else:
    print(-1)