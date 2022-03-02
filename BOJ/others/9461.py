input = __import__('sys').stdin.readline
T = int(input())
N = [int(input()) for _ in range(T)]
DP = [0, 1, 1, 1, 2, 2] + [0] * 95
for i in range(6, 101):
    DP[i] = DP[i - 1] + DP[i - 5]
for x in N: print(DP[x])