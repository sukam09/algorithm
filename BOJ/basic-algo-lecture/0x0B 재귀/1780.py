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
        cur = board[x][y]
        ans[cur] += 1
        return
    for i in range(x, x + n, n // 3):
        for j in range(y, y + n, n // 3):
            solve(i, j, n // 3)

n = ii()
board = [list(mis()) for _ in range(n)]
ans = {-1: 0, 0: 0, 1: 0}
solve(0, 0, n)
for x in ans:
    print(ans[x])