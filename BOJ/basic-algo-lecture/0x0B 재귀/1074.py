import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve(x, y, n):
    global ans
    if (x, y) == (r, c):
        print(ans)
        return
    for i in range(x, x + n, n // 2):
        for j in range(y, y + n, n // 2):
            if i <= r < i + n // 2 and j <= c < j + n // 2:
                solve(i, j, n // 2)
            ans += (n // 2) ** 2
    
n, r, c = mis()
ans = 0
solve(0, 0, 2 ** n)