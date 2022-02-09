import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
d = [float('inf')] * (n + 1)
d[0] = 0
for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        d[i] = min(d[i], d[i - j ** 2] + 1)
print(d[n])