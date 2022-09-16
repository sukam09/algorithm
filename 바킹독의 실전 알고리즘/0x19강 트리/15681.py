import sys
input = lambda: sys.stdin.readline().rstrip()
try:
    sys.stdin = open('input.txt', 'r')
except:
    pass

from collections import defaultdict
sys.setrecursionlimit(10 ** 5)

def dfs(v):
    cnt = 0
    for nv in adj[v]:
        if nv == p[v]:
            continue
        p[nv] = v
        dfs(nv)
        cnt += ans[nv]
    if cnt == 0:
        ans[v] = 1
    else:
        ans[v] = 1 + cnt

n, r, q = map(int, input().split())
adj = defaultdict(list)
p = [0] * (n + 1)
ans = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
dfs(r)
for _ in range(q):
    u = int(input())
    print(ans[u])