from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n + 1))
ans = []

for _ in range(n):
    for _ in range(k - 1):
        q.rotate(-1)
    ans.append(q.popleft())

print('<' + ', '.join(map(str, ans)) + '>')