import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
p = [0] + list(mis())
d = [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = max(d[j] + p[i - j] for j in range(i + 1))
print(d[n])