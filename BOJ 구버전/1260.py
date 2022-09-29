from collections import defaultdict, deque

def dfs():
    for s in adj:
        adj[s].sort(reverse=True)
    s = deque([V])
    visited = [0] * (N + 1)
    ans = []
    while s:
        v = s.pop()
        if visited[v]:
            continue
        visited[v] = 1
        ans.append(v)
        for e in adj[v]:
            if not visited[e]:
                s.append(e)
    return ans

def bfs():
    for s in adj:
        adj[s].sort()
    q = deque([V])
    visited = [0] * (N + 1)
    visited[V] = 1
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = 1
    return ans

N, M, V = map(int, input().split())
adj = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
print(*dfs())
print(*bfs())