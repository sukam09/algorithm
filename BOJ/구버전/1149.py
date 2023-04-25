def RGB(N, R, G, B):
    DP[N][0] = min(DP[N - 1][1:]) + R
    DP[N][1] = min(DP[N - 1][0], DP[N - 1][2]) + G
    DP[N][2] = min(DP[N - 1][:2]) + B
    return DP

input = __import__('sys').stdin.readline
N = int(input())
DP = [[0, 0, 0] for _ in range(1001)]
for i in range(1, N + 1):
    R, G, B = map(int, input().split())
    DP = RGB(i, R, G, B)
print(min(DP[N]))