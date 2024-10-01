import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = []

for i, x in enumerate(arr):
    arr2.append((i + 1, x))

q = deque(arr2)

while q:
    i, x = q.popleft()
    print(i, end=' ')
    if x > 0:
        y = x - 1
        q.rotate(-y)
    else:
        q.rotate(-x)