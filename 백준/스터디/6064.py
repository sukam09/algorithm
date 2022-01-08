from sys import stdin
from math import gcd
input = stdin.readline
lcm = lambda m, n: gcd(m, n) * (m // gcd(m, n)) * (n // gcd(m, n))

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    while x <= lcm(m, n):
        if x % n == y % n:
            print(x)
            break
        x += m
    else:
        print(-1)