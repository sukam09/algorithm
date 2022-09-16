import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve():
    d[0][0] = board[0][0]
    d[1][0] = board[1][0]
    if n == 1:
        return
    d[0][1] = d[1][0] + board[0][1]
    d[1][1] = d[0][0] + board[1][1]
    for i in range(2, n):
        d[0][i] = max(d[1][i - 1], d[1][i - 2]) + board[0][i]
        d[1][i] = max(d[0][i - 1], d[0][i - 2]) + board[1][i]

t = ii()
for _ in range(t):
    n = ii()
    board = [list(mis()) for _ in range(2)]
    d = [[0] * n for _ in range(2)]
    solve()
    print(max(d[0][n - 1], d[1][n - 1]))