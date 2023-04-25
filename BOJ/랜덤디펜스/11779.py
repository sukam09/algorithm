import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
dist = [float('inf')] * (n + 1)
pre = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
st, en = map(int, input().split())
dist[st] = 0
pq = []
heappush(pq, (0, st))
while pq:
    cc, cv = heappop(pq)
    if dist[cv] != cc:
        continue
    for nc, nv in adj[cv]:
        if dist[cv] + nc < dist[nv]:
            dist[nv] = dist[cv] + nc
            heappush(pq, (dist[nv], nv))
            pre[nv] = cv
print(dist[en])
cur = en
hist = [en]
while pre[cur] != st:
    hist.append(pre[cur])
    cur = pre[cur]
hist.append(st)
print(len(hist))
print(*reversed(hist))