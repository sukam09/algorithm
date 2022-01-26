from sys import stdin
input = stdin.readline

s = input().rstrip()
a = []
x = ''
for c in reversed(s):
    x = c + x
    a.append(x)
for x in sorted(a):
    print(x)