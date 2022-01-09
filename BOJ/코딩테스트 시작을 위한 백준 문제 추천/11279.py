from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x:
        heappush(heap, -x)
    else:
        print(-heappop(heap)) if heap else print(0)