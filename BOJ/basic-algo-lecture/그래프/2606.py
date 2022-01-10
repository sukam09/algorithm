from sys import stdin
from collections import defaultdict, deque
input = stdin.readline

n = int(input())
e = int(input())
graph = defaultdict(list)

for _ in range(e):
    st, en = map(int, input().split())
    graph[st].append(en)
    graph[en].append(st)

que = deque([1])
vis = [0] * (n + 5)
vis[1] = 1
ans = 0

while que:
    cur = que.popleft()
    ans += 1
    for nxt in graph[cur]:
        if not vis[nxt]:
            que.append(nxt)
            vis[nxt] = 1

print(ans - 1)