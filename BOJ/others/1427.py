from sys import stdin

input = stdin.readline
N = input().rstrip()
N = sorted(list(N), reverse=True)
for n in N:
    print(n, end='')
