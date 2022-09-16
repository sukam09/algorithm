from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1] + [0] * k

for coin in coins:
	for i in range(coin, k + 1):
		dp[i] += dp[i - coin]

print(dp[k])