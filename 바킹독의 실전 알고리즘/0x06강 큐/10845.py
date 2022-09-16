from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()

    if len(cmd) == 2:
        cmd[1] = int(cmd[1])
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        print(q.popleft()) if q else print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        print(int(not q))
    elif cmd[0] == 'front':
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)