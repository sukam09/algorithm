import sys
from copy import deepcopy
input = sys.stdin.readline

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def OOB(x, y):
    return x < 0 or x >= 4 or y < 0 or y >= 4

def find(x):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == x:
                return i, j, board[i][j][1]
    return -1, -1, -1

def move():
    global board
    for i in range(1, 17):
        x, y, d = find(i)
        if x == -1:
            continue
        for dir in range(8):
            nd = (d + dir) % 8
            nx = x + dx[nd]
            ny = y + dy[nd]
            if OOB(nx, ny) or board[nx][ny][0] == 0:
                continue
            # 위치를 바꾸기 전 바뀐 방향으로 적용
            board[x][y] = (i, nd)
            board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
            break

def dfs(x, y, score):
    global ans, board
    ans = max(ans, score)
    d = board[x][y][1]
    tx = x
    ty = y
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if OOB(nx, ny):
            break
        if board[nx][ny][0] < 1:
            x = nx
            y = ny
            continue
        tmp = deepcopy(board)
        val = board[nx][ny][0]
        board[tx][ty] = (-1, -1)
        board[nx][ny] = (0, board[nx][ny][1])
        move()
        dfs(nx, ny, score + val)
        board = deepcopy(tmp)
        x = nx
        y = ny

board = []
for _ in range(4):
    x = list(map(int, input().split()))
    y = []
    for i in range(0, 8, 2):
        y.append((x[i], x[i + 1] - 1))
    board.append(y)
st = board[0][0][0]
board[0][0] = (0, board[0][0][1])
ans = st
move()
dfs(0, 0, st)
print(ans)