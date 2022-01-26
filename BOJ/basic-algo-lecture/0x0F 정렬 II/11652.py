from sys import stdin
input = stdin.readline

def f(s):
    cnt = 0
    for c in s:
        if c.isdigit():
            cnt += int(c)
    return cnt

n = int(input())
a = [input().rstrip() for _ in range(n)]
a.sort(key=lambda x: (len(x), f(x), x))
for x in a:
    print(x)