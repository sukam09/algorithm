import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
s = 0
for x in c:
    s += x
d = [[0] * (s + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(s + 1):
        if j - c[i] >= 0:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - c[i]] + a[i])
        else:
            d[i][j] = d[i - 1][j]
for j in range(s + 1):
    if d[n][j] >= m:
        print(j)
        break