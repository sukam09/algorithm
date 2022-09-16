import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

d = [0] * 35
n = ii()
d[0], d[2] = 1, 3
for i in range(4, n + 1, 2):
    d[i] += d[i - 2] * 3
    for j in range(i - 4, -1, -2):
        d[i] += d[j] * 2
print(d[n])