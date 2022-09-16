def solution(board):
    r, c = len(board), len(board[0])
    dp = [[0] * c for _ in range(r)]

    for i in range(r):
        dp[i][0] = board[i][0]
    
    for i in range(c):
        dp[0][i] = board[0][i]

    for i in range(1, r):
        for j in range(1, c):
            if board[i][j]:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return max(map(max, dp)) ** 2