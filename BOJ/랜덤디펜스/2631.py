import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
d = [1] * (n + 1)
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)
print(n - max(d))