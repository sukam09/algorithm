input = __import__('sys').stdin.readline
N = int(input())
DP = [[0]*10 for _ in range(N+1)]
for i in range(1, 10): DP[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        if j == 0: DP[i][j+1] += DP[i-1][j]
        elif j == 9: DP[i][j-1] += DP[i-1][j]
        else:
            DP[i][j+1] += DP[i-1][j]
            DP[i][j-1] += DP[i-1][j]
print(sum(DP[N]) % 1000000000)