import sys
input = lambda: sys.stdin.readline().rstrip()
try:
    sys.stdin = open('input.txt', 'r')
except:
    pass

sys.setrecursionlimit(100000)

def dfs(v):
    global cycle
    if vis[v]:
        cycle = True
        return
    vis[v] = 1
    for nv in adj[v]:
        if nv == p[v]:
            continue
        p[nv] = v
        dfs(nv)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
vis = [0] * (n + 1)
p = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    if vis[i]:
        continue
    ans += 1
    cycle = False
    dfs(i)
    if cycle:
        ans += 1
print(ans - 1)