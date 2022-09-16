input = __import__('sys').stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = []
for i, val in enumerate(a):
    while s and s[-1][0] < val:
        s.pop()
    if not s:
        print(0, end=' ')
    else:
        print(s[-1][1], end=' ')
    s.append((val, i + 1))