from sys import stdin
from math import gcd
input = stdin.readline  

e, s, m = map(int, input().split())
em, sm, mm = 15, 28, 19
g = lambda a, b, c: gcd(a, gcd(b, c))
lcm = lambda a, b, c: g(a, b, c) * (a // g(a, b, c)) * (b // g(a, b, c)) * (c // g(a, b, c))
mx = lcm(em, sm, mm)
ey, sy, my = 0, 0, 0

for i in range(1, mx + 1):
    ey += 1
    sy += 1
    my += 1
    
    if ey > em:
        ey = 1
    if sy > sm:
        sy = 1
    if my > mm:
        my = 1
    
    if (ey, sy, my) == (e, s, m):
        print(i)
        break