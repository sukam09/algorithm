from sys import stdin

input = stdin.readline
N = int(input())
n = [int(input()) for _ in range(N)]
for x in sorted(n):
    print(x)
