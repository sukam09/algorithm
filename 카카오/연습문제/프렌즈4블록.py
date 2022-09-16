def search(m, n, board):
    erase = 0
    check = [[0] * n for _ in range(m)]
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == ' ':
                continue
            cur = board[i][j]
            cnt = 0
            for ni, nj in (i + 1, j), (i, j + 1), (i + 1, j + 1):
                if board[ni][nj] == cur:
                    cnt += 1
            if cnt == 3:
                for ni, nj in (i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1):
                    if not check[ni][nj]:
                        check[ni][nj] = 1
                        erase += 1
    return erase, check

def changeboard(m, n, board, check):
    for j in range(n):
        idx = m - 1
        for i in range(m - 1, -1, -1):
            if not check[i][j]:
                board[idx][j] = board[i][j]
                idx -= 1
        for i in range(idx, -1, -1):
            board[i][j] = ' '
    return board

def solution(m, n, board):
    ans = 0
    board = [[board[i][j] for j in range(n)] for i in range(m)]
    while True:
        erase, check = search(m, n, board)
        if erase == 0:
            break
        ans += erase
        board = changeboard(m, n, board, check)
    return ans