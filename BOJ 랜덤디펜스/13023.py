import sys
input = sys.stdin.readline

def dfs(v, d):
    if d > 4:
        return
    if d == 4:
        print(1)
        sys.exit(0)
    for nv in adj[v]:
        if vis[nv]:
            continue
        vis[nv] = 1
        dfs(nv, d + 1)
        vis[nv] = 0

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
vis = [0] * n
for i in range(n):
    vis[i] = 1
    dfs(i, 0)
    vis[i] = 0
print(0)