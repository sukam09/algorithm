from sys import stdin
input = stdin.readline

def f(s):
    s[0] = int(s[0])
    return s

n = int(input())
a = [f(input().split()) for _ in range(n)]
for x in sorted(a, key=lambda x: x[0]):
    print(*x)