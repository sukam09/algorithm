input = __import__('sys').stdin.readline
N = int(input())
score = [0] + [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N+1)]
dp[1][0] = score[1]
for i in range(2, N+1):
    dp[i][0] = max(dp[i-2]) + score[i]
    dp[i][1] = dp[i-1][0] + score[i]
print(max(dp[N]))