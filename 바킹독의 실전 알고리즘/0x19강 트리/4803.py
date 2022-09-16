import sys
input = lambda: sys.stdin.readline().rstrip()
try:
    sys.stdin = open('input.txt', 'r')
except:
    pass

from collections import defaultdict

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

def solve():
    global cycle
    ret = 0
    for i in range(1, n + 1):
        if vis[i]:
            continue
        cycle = False
        dfs(i)
        if not cycle:
            ret += 1
    return ret

tc = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    adj = defaultdict(list)
    vis = [0] * (n + 1)
    p = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    ans = solve()
    print(f"Case {tc}: ", end='')
    if ans == 0:
        print("No trees.")
    elif ans == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {ans} trees.")
    tc += 1