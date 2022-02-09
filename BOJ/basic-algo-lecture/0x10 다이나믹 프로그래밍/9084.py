import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve():
    d = [1] + [0] * m
    for c in a:
        for j in range(1, m + 1):
            if j - c >= 0:
                d[j] += d[j - c]
    print(d[m])

t = ii()
for _ in range(t):
    n = ii()
    a = list(mis())
    m = ii()
    solve()