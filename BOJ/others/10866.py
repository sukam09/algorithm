import sys
from collections import deque

N = int(sys.stdin.readline())
commands = [sys.stdin.readline().split() for _ in range(N)]
d = deque()

for command in commands:
    if len(command) == 2:  # push
        c, item = command[0], command[1]
        if c == 'push_front':
            d.appendleft(item)
        else:  # push_back
            d.append(item)
    else:
        c = command[0]
        if c == 'pop_front':
            if len(d) > 0:
                print(d.popleft())
            else:
                print(-1)
        elif c == 'pop_back':
            if len(d) > 0:
                print(d.pop())
            else:
                print(-1)
        elif c == 'size':
            print(len(d))
        elif c == 'empty':
            is_empty = 1 if len(d) == 0 else 0
            print(is_empty)
        elif c == 'front':
            if len(d) > 0:
                print(d[0])
            else:
                print(-1)
        else:  # back
            if len(d) > 0:
                print(d[-1])
            else:
                print(-1)