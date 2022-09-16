from sys import stdin
input = stdin.readline

mx = 10 ** 6 + 1
t = mx
a = []
while t:
    s = input().split()
    a += s
    if t == mx:
        t = int(s[0])
        t -= len(s) - 1
    else:
        t -= len(s)
a = a[1:]
rev = lambda n: int(n[::-1])
for x in sorted(map(rev, a)):
    print(x)