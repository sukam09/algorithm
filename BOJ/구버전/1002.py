import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if d == 0:
        ans = -1 if r1 == r2 else 0
    elif d > r1 + r2:
        ans = 0
    elif d == r1 + r2:
        ans = 1
    else:
        if d < abs(r1 - r2):
            ans = 0
        elif d == abs(r1 - r2):
            ans = 1
        else:
            ans = 2

    # elif d < r1 + r2:
    #     ans = 2
    # elif d == abs(r1 - r2):
    #     ans = 1
    # elif d < abs(r1 - r2):
    #     ans = 0

    print(ans)
