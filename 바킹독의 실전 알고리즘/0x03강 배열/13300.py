from sys import stdin
from math import ceil
input = stdin.readline

n, k = map(int, input().split())
a = [[0] * 7 for _ in range(11)]
for _ in range(n):
    s, y = map(int, input().split())
    a[y][s] += 1

ans = 0
for i in range(1, 7):
    for j in range(2):
        ans += ceil(a[i][j] / k)
print(ans)