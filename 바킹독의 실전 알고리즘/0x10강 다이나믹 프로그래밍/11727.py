import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
d = [0] * (n + 1)
d[0] = d[1] = 1
for i in range(2, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 10007
print(d[n])