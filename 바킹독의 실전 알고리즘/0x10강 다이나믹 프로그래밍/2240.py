import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

t, w = mis()
a = [0] + [ii() for _ in range(t)]
d = [[0] * 35 for _ in range(1005)]
for i in range(w + 1):
    d[1][i] = a[1] - 1 if i % 2 else 2 - a[1]
cnt = 0
for i in range(1, t + 1):
    if a[i] == 1: cnt += 1
    d[i][0] = cnt
for i in range(2, t + 1):
    for j in range(1, w + 1):
        val = max(d[i - 1][k] for k in range(j + 1))
        d[i][j] = val + (1 + j % 2 == a[i])
print(max(d[t]))