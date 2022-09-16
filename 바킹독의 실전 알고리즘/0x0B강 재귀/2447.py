import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve(x, y, n):
    if n == 1:
        board[x][y] = '*'
        return
    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1):
                continue
            solve(x + n // 3 * i, y + n // 3 * j, n // 3)

n = ii()
board = [[' '] * n for _ in range(n)]
solve(0, 0, n)
for i in range(n):
    for j in range(n):
        print(board[i][j], end='')
    print()