from collections import defaultdict
from collections import deque

def solution(n, edge):
    graph = defaultdict(list)

    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    vis = [0] * (n + 1)
    vis[1] = 1
    q = deque([(1, 0)])
    dist_list = []

    while q:
        v, dist = q.popleft()
        dist_list.append(dist)
        for nv in graph[v]:
            if not vis[nv]:
                q.append((nv, dist + 1))
                vis[nv] = 1

    return dist_list.count(max(dist_list))