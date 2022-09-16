from sys import stdin

input = stdin.readline
N = int(input())
T = []
P = []
profit = [0] * N
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    if i == 0:
        profit[0] = P[0] if T[0] <= N else 0
        continue
    maxval = 0
    for j in range(i):
        res = profit[j] + P[i] if T[j] <= i - j and i + T[i] <= N else profit[j]
        if res > maxval:
            maxval = res
    profit[i] = maxval
print(profit[N - 1])