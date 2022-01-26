from sys import stdin
input = stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
for x in sorted(a):
    print(x)