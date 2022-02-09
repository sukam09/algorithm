import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

d = [0, 1, 2, 4] + [0] * 1000000
for i in range(4, 1000001):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % (10 ** 9 + 9)
t = ii()
for _ in range(t):
    n = ii()
    print(d[n])