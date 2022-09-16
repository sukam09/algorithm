from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
s = []
seq = deque([int(input()) for _ in range(n)])
ans = []
num = 1

while seq:
    if not s or s[-1] < seq[0]:
        s.append(num)
        ans.append('+')
        num += 1
    elif s[-1] == seq[0]:
        s.pop()
        ans.append('-')
        seq.popleft()
    else:
        print("NO")
        break
    
else:
    for op in ans:
        print(op)