from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
Q = deque()
for _ in range(n):
    op = input().split()
    if len(op) == 2:
        x = int(op[1])
        Q.append(x)
    else:
        op = op[0]
        if op == 'pop':
            print(Q.popleft() if Q else -1)
        elif op == 'size':
            print(len(Q))
        elif op == 'empty':
            print(int(not Q))
        elif op == 'front':
            print(Q[0] if Q else -1)
        else:
            print(Q[-1] if Q else -1)