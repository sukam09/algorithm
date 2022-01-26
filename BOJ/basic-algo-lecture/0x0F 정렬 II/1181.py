from sys import stdin
input = stdin.readline

n = int(input())
a = set(input().rstrip() for _ in range(n))
for x in sorted(a, key=lambda x: (len(x), x)):
    print(x)