def solution(triangle):
    n = len(triangle)
    for i in range(len(triangle)):
        triangle[i] = [-1] + triangle[i]
    triangle = [[-1]] + triangle
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == 1:
            dp[i][1] = triangle[1][1]
        elif i == 2:
            dp[i][1] = triangle[1][1] + triangle[2][1]
            dp[i][2] = triangle[1][1] + triangle[2][2]
        else:
            dp[i][1] = dp[i - 1][1] + triangle[i][1]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
            for j in range(1, i):
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    return max(dp[n])