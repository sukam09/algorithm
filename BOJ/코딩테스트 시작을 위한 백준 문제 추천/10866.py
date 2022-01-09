from sys import stdin
from collections import deque
input = stdin.readline

q = deque()
n = int(input())

for _ in range(n):
    cmd = input().split()
    
    if len(cmd) == 2:
        cmd[1] = int(cmd[1])
        if cmd[0] == 'push_front':
            q.appendleft(cmd[1])
        else:
            q.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(q.popleft()) if q else print(-1)
    elif cmd[0] == 'pop_back':
        print(q.pop()) if q else print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        print(int(not q))
    elif cmd[0] == 'front':
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)