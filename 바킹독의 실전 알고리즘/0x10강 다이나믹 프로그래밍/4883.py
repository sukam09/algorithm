import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve():
    d = [[0, 0, 0]] + [list(mis()) for _ in range(n)]
    d[1][2] += d[1][1]
    d[2][0] += d[1][1]
    d[2][1] += min(d[2][0], d[1][1], d[1][2])
    d[2][2] += min(d[2][1], d[1][1], d[1][2])
    for i in range(3, n + 1):
        d[i][0] += min(d[i - 1][0], d[i - 1][1])
        d[i][1] += min(d[i][0], min(d[i - 1][j] for j in range(3)))
        d[i][2] += min(d[i][1], d[i - 1][1], d[i - 1][2])
    return d[n][1]

k = 1
while True:
    n = ii()
    if n == 0:
        break
    ans = solve()
    print(f"{k}. {ans}")
    k += 1