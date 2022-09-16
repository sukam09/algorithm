import sys
input = lambda: sys.stdin.readline().rstrip()
try:
    sys.stdin = open('input.txt', 'r')
except:
    pass

from collections import defaultdict

def dfs(v):
    global st, en
    if v == en:
        print(dist[(st, v)])
    for nv in adj[v]:
        if nv == p[v]:
            continue
        p[nv] = v
        dist[(st, nv)] = dist[(st, v)] + dist[(v, nv)]
        dfs(nv)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
dist = defaultdict(int)
for _ in range(n - 1):
    u, v, d = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    dist[(u, v)] = d
    dist[(v, u)] = d
for _ in range(m):
    u, v = map(int, input().split())
    p = [0] * (n + 1)
    st, en = u, v
    dfs(st)