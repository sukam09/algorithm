from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(n, start, graph):
    h = []
    heappush(h, (0, start))
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    while h:
        d, s = heappop(h)
        if dist[s] < d:
            continue
            
        for e, c in graph[s]:
            if d + c < dist[e]:
                dist[e] = d + c
                heappush(h, (d + c, e))
    
    return dist

def solution(n, a, s, b, fares):
    graph = defaultdict(list)
    dist = {}
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    for i in range(1, n + 1):
        dist[i] = dijkstra(n, i, graph)

    ans = float('inf')
    for i in range(1, n + 1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    
    return ans