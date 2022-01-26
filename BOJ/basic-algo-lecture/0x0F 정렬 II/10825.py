from sys import stdin
input = stdin.readline

def f(s):
    for i in range(1, 4):
        s[i] = int(s[i])
    return s

n = int(input())
a = [f(input().split()) for _ in range(n)]
for x in sorted(a, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(x[0])