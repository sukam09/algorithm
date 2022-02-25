import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

d = [[0] * 1005 for _ in range(1005)]
MOD = 1000000003
n = ii()
k = ii()
for i in range(1, n + 1): d[i][1] = i
for i in range(4, n + 1):
    for j in range(2, k + 1):
        if j > i / 2: continue
        d[i][j] = (d[i - 1][j] + d[i - 2][j - 1]) % MOD
print(d[n][k])