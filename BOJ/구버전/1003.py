input = __import__('sys').stdin.readline
T = int(input())
N = [int(input()) for _ in range(T)]
ans = {0: (1, 0)}
for i in range(1, max(N) + 1):
    ans[i] = (ans[i - 1][1], ans[i - 1][0] + ans[i - 1][1])
for x in N: print(*ans[x])