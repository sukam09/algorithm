def chkh(x, y):
    if oob(x, y + 1) or board[x][y + 1]:
        return False
    return True

def chkv(x, y):
    if oob(x + 1, y) or board[x + 1][y]:
        return False
    return True

def chkd(x, y):
    if oob(x + 1, y + 1) or board[x][y + 1] or board[x + 1][y] or board[x + 1][y + 1]:
        return False
    return True

def sim(x, y, c):
    global ans
    if (x, y) == (n - 1, n - 1):
        ans += 1
        return
    
    if c == 0:
        if chkh(x, y):
            sim(x, y + 1, 0)
        if chkd(x, y):
            sim(x + 1, y + 1, 2)
    elif c == 1:
        if chkv(x, y):
            sim(x + 1, y, 1)
        if chkd(x, y):
            sim(x + 1, y + 1, 2)
    else:
        if chkh(x, y):
            sim(x, y + 1, 0)
        if chkv(x, y):
            sim(x + 1, y, 1)
        if chkd(x, y):
            sim(x + 1, y + 1, 2)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
oob = lambda x, y: x < 0 or x >= n or y < 0 or y >= n
if board[n - 1][n - 1]:
    print(0)
else:
    sim(0, 1, 0)
    print(ans)