import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve(cur):
    global ans
    if cur == n:
        ans += 1
        return
    for i in range(n):
        if c[i] or d1[cur + i] or d2[cur - i + n - 1]:
            continue
        c[i] = 1
        d1[cur + i] = 1
        d2[cur - i + n - 1] = 1
        solve(cur + 1)
        c[i] = 0
        d1[cur + i] = 0
        d2[cur - i + n - 1] = 0

n = ii()
board = [[0] * n for _ in range(n)]
c = [0] * n
d1 = [0] * (2 * n - 1)
d2 = [0] * (2 * n - 1)
ans = 0
solve(0)
print(ans)