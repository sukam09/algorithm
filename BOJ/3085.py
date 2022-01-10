def swap(a, b, c, d):
    board[a][b], board[c][d] = board[c][d], board[a][b]

def search():
    n = len(board)
    maxcnt = 1
    cnt = 1
    
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
                maxcnt = max(cnt, maxcnt)
            else:
                cnt = 1
    
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
                maxcnt = max(cnt, maxcnt)
            else:
                cnt = 1

    return maxcnt

n = int(input())
board = [list(input()) for _ in range(n)]
ans = 1

for i in range(n):
    for j in range(n - 1):
        if board[i][j] != board[i][j + 1]:
            swap(i, j, i, j + 1)
            ans = max(search(), ans)
            swap(i, j, i, j + 1)

for i in range(n - 1):
    for j in range(n):
        if board[i][j] != board[i + 1][j]:
            swap(i, j, i + 1, j)
            ans = max(search(), ans)
            swap(i, j, i + 1, j)

print(ans)