import sys
from collections import deque

N = int(sys.stdin.readline())
commands = [sys.stdin.readline().split() for _ in range(N)]
queue = deque()
for command in commands:
    if len(command) == 2:  # push
        item = command[1]
        queue.append(item)
    else:
        c = command[0]
        if c == 'pop':
            if len(queue) > 0:
                print(queue.popleft())
            else:
                print(-1)
        elif c == 'size':
            print(len(queue))
        elif c == 'empty':
            is_empty = 1 if len(queue) == 0 else 0
            print(is_empty)
        elif c == 'front':
            if len(queue) > 0:
                print(queue[0])
            else:
                print(-1)
        else:  # back
            if len(queue) > 0:
                print(queue[-1])
            else:
                print(-1)