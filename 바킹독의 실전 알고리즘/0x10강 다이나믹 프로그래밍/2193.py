import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
d = [[0] * 2 for _ in range(n + 1)]
d[1][1] = 1
for i in range(2, n + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1]
    d[i][1] = d[i - 1][0]
print(sum(d[n]))