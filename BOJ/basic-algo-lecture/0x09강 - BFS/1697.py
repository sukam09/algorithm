from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
vis = [0] * 100002
oob = lambda x: x < 0 or x > 100000
que = deque([(n, 0)])
vis[n] = 1

while que:
    cur, ans = que.popleft()
    if cur == k:
        break
    for nxt in cur - 1, cur + 1, cur * 2:
        if not oob(nxt) and not vis[nxt]:
            que.append((nxt, ans + 1))
            vis[nxt] = 1

print(ans)