import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n = ii()
d = [-1, 0, 1, 0, 0] + [-1] * n
ans = ['SK', 'CY']
for i in range(5, n + 1):
    for j in 1, 3, 4:
        if d[i - j]:
            d[i] = 0
            break
    else:
        d[i] = 1
print(ans[d[n]])