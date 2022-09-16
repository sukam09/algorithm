from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)

    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    vis = [0] * (n + 1)
    vis[1] = 1
    q = deque([(1, 0)])
    dist = []

    while q:
        v, d = q.popleft()
        dist.append(d)
        for nv in graph[v]:
            if not vis[nv]:
                q.append((nv, d + 1))
                vis[nv] = 1

    return dist.count(max(dist))