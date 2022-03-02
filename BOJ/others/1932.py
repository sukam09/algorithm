input = __import__('sys').stdin.readline
n = int(input())
base = [[-1]]
triangle = [[-1] + list(map(int, input().split())) for _ in range(n)]
triangle = base + triangle
dp = [[-1] * (i + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    if i == 1: dp[1][1] = triangle[1][1]
    elif i == 2:
        dp[2][1] = dp[1][1] + triangle[2][1]
        dp[2][2] = dp[1][1] + triangle[2][2]
    else:
        dp[i][1] = dp[i - 1][1] + triangle[i][1]
        dp[i][-1] = dp[i - 1][-1] + triangle[i][-1]
        for j in range(2, i):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
print(max(dp[n]))