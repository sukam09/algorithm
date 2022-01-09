from sys import stdin
input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n + 5)] for _ in range(n + 5)]

for i in range(1, n):
    if board[0][i]:
        break
    dp[0][i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        if board[i][j]:
            continue
        dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
        if board[i - 1][j] or board[i][j - 1]:
            continue
        dp[i][j][2] = sum(dp[i - 1][j - 1])

print(sum(dp[n - 1][n - 1]))