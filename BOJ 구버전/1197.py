from sys import stdin
import heapq

input = stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))
vis = [0] * (V + 1)
ans = 0
vis[1] = 1
h = graph[1]
heapq.heapify(h)
while h:
    c, v = heapq.heappop(h)
    if not vis[v]:
        ans += c
        vis[v] = 1
        for c, nv in graph[v]:
            if not vis[nv]:
                heapq.heappush(h, (c, nv))
print(ans)