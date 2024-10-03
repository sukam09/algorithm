import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    for x in temp[1:]:
        adj[i].append(x)

vis = [0] * (n + 1)
blue = 0
red = 0
picked = 0
blue_cnt = 0
red_cnt = 0

def bfs_blue(v):
    global blue_cnt, blue
    vis[v] = 1
    q = deque([v])
    while q:
        x = q.popleft()
        blue_cnt += 1
        blue += arr[x]
        for nx in adj[x]:
            if vis[nx] or nx not in cand:
                continue
            vis[nx] = 1
            q.append(nx)

def bfs_red(v):
    global red_cnt, red
    vis[v] = 1
    q = deque([v])
    while q:
        x = q.popleft()
        red_cnt += 1
        red += arr[x]
        for nx in adj[x]:
            if vis[nx] or nx in cand:
                continue
            vis[nx] = 1
            q.append(nx)

def solve():
    global ans, blue_cnt, red_cnt, blue, red
    bi = -1
    ri = -1
    blue_cnt = 0
    red_cnt = 0
    blue = 0
    red = 0
    for i in range(1, n + 1):
        if i in cand and bi == -1:
            bi = i
        if i not in cand and ri == -1:
            ri = i
    for i in range(1, n + 1):
        vis[i] = 0
    bfs_blue(bi)
    bfs_red(ri)
    if blue_cnt != picked:
        return
    if red_cnt != n - picked:
        return
    ans = min(ans, abs(blue - red))

ans = float('inf')
for i in range(1, n // 2 + 1):
    for cb in combinations(range(1, n + 1), i):
        cand = set(cb)
        picked = i
        solve()

print(ans if ans != float('inf') else -1)