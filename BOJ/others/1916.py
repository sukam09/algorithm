from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop

input = stdin.readline
N = int(input())
M = int(input())
graph = defaultdict(list)
dist = [float('inf')]*(N+1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
start, end = map(int, input().split())
h = []
heappush(h, (0, start)); dist[start] = 0
while h:
    cost, start = heappop(h)
    if dist[start] < cost: continue
    for e, c in graph[start]:
        if cost+c < dist[e]:
            dist[e] = cost+c
            heappush(h, (cost+c, e))
print(dist[end])