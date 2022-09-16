import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())
print = sys.stdout.write

def solve(x, y, n):
    if n == 3:
        board[x][y + 2] = '*'
        board[x + 1][y + 1] = '*'
        board[x + 1][y + 3] = '*'
        for i in range(5):
            board[x + 2][y + i] = '*'
        return

    k = 6 * (n // 3) - 1
    solve(x, y + (k + 1) // 4, n // 2)
    solve(x + n // 2, y, n // 2)
    solve(x + n // 2, y + (k + 1) // 2, n // 2)

n = ii()
k = 6 * (n // 3) - 1
board = [[' '] * k for _ in range(n)]
solve(0, 0, n)
for i in range(n):
    for j in range(k):
        print(board[i][j])
    print('\n')