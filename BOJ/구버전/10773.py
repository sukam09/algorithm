import sys
from collections import deque

K = int(sys.stdin.readline())
d = deque()
for _ in range(K):
    n = int(sys.stdin.readline())
    if n > 0:
        d.append(n)
    else:
        d.pop()
print(sum(d))