from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(N, town):
    h = []
    heappush(h, (0, 1))
    distance = [float('inf')] * (N + 1)
    distance[1] = 0
    
    while h:
        dist, start = heappop(h)
        if distance[start] < dist:
            continue

        for end, cost in town[start]:
            if dist + cost < distance[end]:
                distance[end] = dist + cost
                heappush(h, (dist + cost, end))
    
    return distance

def solution(N, road, K):
    town = defaultdict(list)

    for a, b, c in road:
        town[a].append((b, c))
        town[b].append((a, c))

    distance = dijkstra(N, town)
    return len([dist for dist in distance if dist <= K])