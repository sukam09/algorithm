import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
a = list(mis())
d = [0] * n
d[0] = a[0]
for i in range(1, n):
    d[i] = max(d[i - 1] + a[i], a[i])
print(max(d))