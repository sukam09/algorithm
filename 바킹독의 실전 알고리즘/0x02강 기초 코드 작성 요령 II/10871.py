from sys import stdin
input = stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))
for val in a:
    if val < x:
        print(val, end=' ')