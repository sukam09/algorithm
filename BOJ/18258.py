from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    c = input().split()
    if c[0] == 'push':
        q.append(c[1])
    else:
        c = c[0]
        if c == 'pop':
            print(q.popleft() if q else -1)
        elif c == 'size':
            print(len(q))
        elif c == 'empty':
            print(0 if q else 1)
        elif c == 'front':
            print(q[0] if q else -1)
        else:
            print(q[-1] if q else -1)