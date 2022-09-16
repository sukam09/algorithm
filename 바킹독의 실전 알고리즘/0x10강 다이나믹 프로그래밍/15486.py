import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
t = [0]
p = [0]
for _ in range(n):
    ti, pi = mis()
    t.append(ti)
    p.append(pi)

d = [0] * (n + 2)
for i in range(n, 0, -1):
    if i + t[i] <= n + 1:
        d[i] = max(d[i + t[i]] + p[i], d[i + 1])
    else:
        d[i] = d[i + 1]
print(max(d))