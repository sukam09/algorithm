from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
q = deque(range(1, n + 1))
while len(q) > 1:
    q.popleft()
    q.rotate(-1)
print(q[0])