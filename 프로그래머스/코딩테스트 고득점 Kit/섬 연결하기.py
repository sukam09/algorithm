import heapq

def solution(n, costs):
    graph = [[] for _ in range(n)]
    for s, e, c in costs:
        graph[s].append((c, e))
        graph[e].append((c, s))
    vis = [0] * n
    vis[0] = 1
    h = graph[0]
    heapq.heapify(h)
    ans = 0
    while h:
        c, v = heapq.heappop(h)
        if not vis[v]:
            ans += c
            vis[v] = 1
            for c, nv in graph[v]:
                if not vis[nv]:
                    heapq.heappush(h, (c, nv))
    return ans