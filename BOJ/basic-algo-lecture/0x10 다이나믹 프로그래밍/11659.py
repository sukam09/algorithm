input = __import__('sys').stdin.readline
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n, m = mis()
a = [0] + list(mis())
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
for _ in range(m):
    i, j = mis()
    print(s[j] - s[i - 1])