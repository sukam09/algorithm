"""
1. 방문한 정점을 list에 넣는 방법도 있지만 바로 print하는 방법이 훨씬 더 구현이 쉬움.
2. dfs에서 정점 v를 방문하고 중복 체크를 하는 방법도 있지만 dfs(nv)를 호출하기 전에
   nv에 대해 중복 체크를 하는 방법도 있음.
3. 단, 2와 같은 방법을 쓰려면 dfs(v)를 실행하기 전에 dfs_vis[nv] = 1을 먼저 해줘야 함.
"""

from sys import stdin
from collections import defaultdict, deque
input = stdin.readline

def dfs(v):
    print(v, end=' ')

    for nv in graph[v]:
        if not dfs_vis[nv]:
            dfs_vis[nv] = 1
            dfs(nv)

def bfs(v):
    bfs_vis = [0] * (n + 1)
    bfs_vis[v] = 1
    q = deque([v])

    while q:
        x = q.popleft()
        print(x, end=' ')

        for nx in graph[x]:
            if not bfs_vis[nx]:
                q.append(nx)
                bfs_vis[nx] = 1

n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph:
    graph[key].sort()

dfs_vis = [0] * (n + 1)
dfs_vis[v] = 1

dfs(v)
print()
bfs(v)