from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = set([int(input()) for _ in range(n)])
dp = [-1] * (k + 1)
dp[0] = 0

for i in range(1, k + 1):
    cand = [dp[i - coin] for coin in coins if i >= coin if dp[i - coin] != -1]
    if cand:
        dp[i] = min(cand) + 1

print(dp[k])