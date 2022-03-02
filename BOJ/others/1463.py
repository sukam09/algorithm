input = __import__('sys').stdin.readline
N = int(input())
dp = [0] * (N+1)
dp[0] = float('inf')
for i in range(2, N+1):
    cnt = 0; target = i
    c1 = target // 3 if target % 3 == 0 else 0
    c2 = target // 2 if target % 2 == 0 else 0
    c3 = target - 1
    dp[i] = min(dp[c1], dp[c2], dp[c3]) + 1
print(dp[N])