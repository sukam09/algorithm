import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n, m = mis()
board = [list(map(int, input())) for _ in range(n)]
d = [[0] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            d[i][j] = board[i][j]
        elif board[i][j]:
            d[i][j] = min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1
        ans = max(ans, d[i][j])
print(ans * ans)