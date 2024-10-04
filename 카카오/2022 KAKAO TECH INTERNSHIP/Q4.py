from heapq import heappush, heappop

MX = 0x7f7f7f7f

def solution(n, paths, gates, summits):
    adj = [[] for _ in range(n + 1)]
    for path in paths:
        i, j, w = path
        adj[i].append((w, j))
        adj[j].append((w, i))
    
    d = [MX] * 50005
    is_summit = [0] * 50005
    
    for summit in summits:
        is_summit[summit] = 1
    
    pq = []
    for gate in gates:
        d[gate] = 0
        heappush(pq, (0, gate))
    
    while pq:
        w, v = heappop(pq)
        if w != d[v]:
            continue
        for nw, nv in adj[v]:
            if max(d[v], nw) < d[nv]:
                d[nv] = max(d[v], nw)
                if not is_summit[nv]:
                    heappush(pq, (d[nv], nv))
    
    summits.sort()
    ans = summits[0]
    for summit in summits:
        if d[summit] < d[ans]:
            ans = summit
    return [ans, d[ans]]