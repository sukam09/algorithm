import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

d = [0, 1] + [0] * 1000000
mod = 10 ** 9
n = ii()
for i in range(2, abs(n) + 1):
    d[i] = (d[i - 1] + d[i - 2]) % mod
if n < 0 and -n % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(d[abs(n)] % mod)