import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
m = ii()
v = [0] + [ii() for _ in range(m)] + [n + 1]
d = [1, 1, 2] + [0] * n
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
ans = 1
for i in range(1, len(v)):
    ans *= d[v[i] - v[i - 1] - 1]
print(ans)