import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')
for i in range(3):
    d = [[float('inf')] * 3 for _ in range(n)]
    d[0][i] = a[0][i]
    for j in range(1, n):
        for x in range(3):
            for y in range(3):
                if x == y: continue
                d[j][x] = min(d[j][x], a[j][x] + d[j - 1][y])
    for k in range(3):
        if i != k:
            ans = min(ans, d[-1][k])
print(ans)