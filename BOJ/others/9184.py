from collections import defaultdict
dp = defaultdict(list)

def w(a, b, c):
    if dp[(a, b, c)]: return dp[(a, b, c)]
    else:
        if a <= 0 or b <= 0 or c <= 0: res = 1
        elif a > 20 or b > 20 or c > 20: res = w(20, 20, 20)
        elif a < b < c:
            res = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            res = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        dp[(a, b, c)] = res; return res

input = __import__('sys').stdin.readline
while 1:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))