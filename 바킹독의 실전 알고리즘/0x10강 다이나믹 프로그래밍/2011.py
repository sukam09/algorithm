import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

a = [0] * 5005
d = [0] * 5005
MOD = 1000000

s = input()
n = len(s)
for i in range(1, n + 1):
    a[i] = int(s[i - 1])
d[0] = 1
for i in range(1, n + 1):
    if a[i] > 0: d[i] = (d[i] + d[i - 1]) % MOD
    x = a[i - 1] * 10 + a[i]
    if 10 <= x <= 26:
        d[i] = (d[i] + d[i - 2]) % MOD
print(d[n])