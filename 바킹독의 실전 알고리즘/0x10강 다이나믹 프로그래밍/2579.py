import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
s = [0] + [ii() for _ in range(n)]
d = [[0] * 3 for _ in range(n + 1)]
d[1][1] = s[1]
for i in range(2, n + 1):
    d[i][1] = max(d[i - 2]) + s[i]
    d[i][2] = d[i - 1][1] + s[i]
print(max(d[n]))