from heapq import heappush, heappop

input = __import__('sys').stdin.readline
N = int(input()); h = []
for _ in range(N):
    x = int(input())
    if x: heappush(h, x)
    elif h: print(heappop(h))
    else: print(0)