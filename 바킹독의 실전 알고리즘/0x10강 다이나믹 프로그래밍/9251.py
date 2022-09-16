import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

a = ' ' + input()
b = ' ' + input()
la, lb = len(a), len(b)
d = [[0] * lb for _ in range(la)]
for i in range(1, la):
    for j in range(1, lb):
        if a[i] == b[j]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])
print(d[-1][-1])