from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    while x <= m * n:
        if x % n == y % n:
            print(x)
            break
        x += m
    else:
        print(-1)