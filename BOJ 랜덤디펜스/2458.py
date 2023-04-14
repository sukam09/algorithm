import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
p = [[] for _ in range(n + 1)]
c = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    p[a].append(b)
    c[b].append(a)

def solve():
    global vis1, vis2, cnt1, cnt2
    cnt1 = 0
    cnt2 = 0
    vis1 = [0] * (n + 1)
    vis2 = [0] * (n + 1)
    vis1[cur] = 1
    vis2[cur] = 1
    up(cur)
    down(cur)
    if cnt1 + cnt2 == n - 1:
        return 1
    else:
        return 0

def up(v):
    global cnt1
    if v != cur:
        cnt1 += 1
    for nv in p[v]:
        if vis1[nv]: continue
        vis1[nv] = 1
        up(nv)

def down(v):
    global cnt2
    if v != cur:
        cnt2 += 1
    for nv in c[v]:
        if vis2[nv]: continue
        vis2[nv] = 1
        down(nv)

ans = 0
for i in range(1, n + 1):
    cur = i
    if solve(): ans += 1
print(ans)