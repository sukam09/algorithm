import sys
from collections import deque

a, b = map(int, input().split())
que = deque([(a, 1)])

while que:
    cur, ans = que.popleft()
    for nxt in cur * 2, cur * 10 + 1:
        if nxt > b:
            break
        if nxt == b:
            print(ans + 1)
            sys.exit(0)
        que.append((nxt, ans + 1))

print(-1)