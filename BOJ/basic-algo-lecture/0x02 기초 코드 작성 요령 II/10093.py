from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
print(max(b - a - 1, 0))
for i in range(a + 1, b):
    print(i, end=' ')