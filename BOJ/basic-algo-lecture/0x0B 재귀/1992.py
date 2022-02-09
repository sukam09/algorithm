import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())
sys.stdin = open('input.txt', 'r')

def chk(x, y, n):
    cur = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != cur:
                return False
    return True

def solve(x, y, n):
    if chk(x, y, n):
        print(board[x][y], end='')
        return
    print('(', end='')
    for i in range(x, x + n, n // 2):
        for j in range(y, y + n, n // 2):
            solve(i, j, n // 2)
    print(')', end='')

n = ii()
board = [list(map(int, input())) for _ in range(n)]
solve(0, 0, n)