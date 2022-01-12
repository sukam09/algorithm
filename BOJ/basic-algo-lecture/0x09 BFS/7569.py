from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m, h = map(int, input().split())
for i in range(h):
    for j in range(n):
        map