import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
d = [[0] * 10 for _ in range(n + 1)]
for i in range(10):
    d[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        d[i][j] = (d[i - 1][j] + d[i][j - 1]) % 10007
print(sum(d[n]) % 10007)