from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
d = deque(range(1, n + 1))
ans = 0
queries = list(map(int, input().split()))
for query in queries:
    i = d.index(query)
    left = i
    right = len(d) - i
    if left <= right:
        d.rotate(-left)
        ans += left
    else:
        d.rotate(right)
        ans += right
    d.popleft()
print(ans)