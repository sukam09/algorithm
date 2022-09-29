input = __import__('sys').stdin.readline
N = int(input())
DP = [0] * 1000001
for i in range(1, N + 1):
    if i <= 2: DP[i] = i
    else: DP[i] = (DP[i - 1] + DP[i - 2]) % 15746
print(DP[N])