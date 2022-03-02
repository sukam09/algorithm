N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = 0
cur = cost[0]
for i in range(N - 1):
    ans += cur * distance[i]
    if cost[i + 1] < cur:
        cur = cost[i + 1]
print(ans)