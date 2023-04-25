from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1
q = deque()
for i in range(1, N + 1):
    if degree[i] == 0:
        q.append(i)
ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    for next in graph[cur]:
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)
print(*ans)