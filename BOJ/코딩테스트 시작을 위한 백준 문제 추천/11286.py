from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
heap = []
ans = []
for _ in range(n):
    x = int(input())
    if x == 0:
        print(heappop(heap)[1]) if heap else print(0)
    else:
        heappush(heap, (abs(x), x))