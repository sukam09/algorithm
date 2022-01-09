from sys import stdin
from math import lcm
input = stdin.readline  

e, s, m = map(int, input().split())
em, sm, mm = 15, 28, 19
maxval = lcm(em, sm, mm)
ey, sy, my = 0, 0, 0

for i in range(1, maxval + 1):
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