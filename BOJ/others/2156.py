input = __import__('sys').stdin.readline
n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n+1)]
dp[1][0] = wine[1]
for i in range(2, n+1):
    dp[i][0] = max(dp[i-2]) + wine[i]
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = max(dp[i-1])
print(max(dp[n]))