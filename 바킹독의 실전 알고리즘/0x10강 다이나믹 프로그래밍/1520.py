import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

d = [[-1] * 505 for _ in range(505)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def oob(x, y):
    return x < 0 or x >= m or y < 0 or y >= n

def solve(x, y):
    if x == m - 1 and y == n - 1: return 1
    if d[x][y] != -1: return d[x][y]
    d[x][y] = 0
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if oob(nx, ny) or a[x][y] <= a[nx][ny]: continue
        d[x][y] += solve(nx, ny)
    return d[x][y]

m, n = mis()
a = [list(mis()) for _ in range(m)]
print(solve(0, 0))