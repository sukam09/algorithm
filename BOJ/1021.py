input = __import__('sys').stdin.readline
from collections import deque

N, M = map(int, input().split())
num = deque(list(map(int, input().split())))
Q = deque([i + 1 for i in range(N)])
cnt = 0
while num:
    top = Q[0]
    target = num[0]
    if top == target:
        Q.popleft()
        num.popleft()
    else:
        target_idx = list(Q).index(target)
        if target_idx < len(Q) / 2: Q.rotate(-1)
        else: Q.rotate(1)
        cnt += 1
print(cnt)