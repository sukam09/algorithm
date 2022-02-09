import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve():
    ans = 0
    for i in range(x1, x2 + 1):
        ans += d[i][y2] - d[i][y1 - 1]
    print(ans)
    
n, m = mis()
board = [[0] * n] + [[0] + list(mis()) for _ in range(n)]
d = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        d[i][j] = d[i][j - 1] + board[i][j]
for _ in range(m):
    x1, y1, x2, y2 = mis()
    solve()