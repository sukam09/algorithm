import sys
from collections import deque
input = sys.stdin.readline

def solve(graph):
    vis = [0] * len(graph)
    vis[0] = 1
    q = deque([(graph[0][0], graph[0][1])])
    while q:
        x, y = q.popleft()
        if abs(x - graph[-1][0]) + abs(y - graph[-1][1]) <= 1000:
            print('happy')
            return
        for i in range(1, len(graph) - 1):
            if vis[i]: continue
            if abs(x - graph[i][0]) + abs(y - graph[i][1]) > 1000:
                continue
            vis[i] = 1
            q.append((graph[i][0], graph[i][1]))
    print('sad')

t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n + 2):
        x, y = map(int, input().split())
        graph.append((x, y))
    solve(graph)