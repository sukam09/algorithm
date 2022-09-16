from sys import stdin
from collections import Counter
input = stdin.readline

n, c = map(int, input().split())
a = list(map(int, input().split()))
cnt = Counter(a)
b = []
s = list(set(a))
for i, val in enumerate(s):
    b.append((cnt[val], i))
for x in sorted(b, key=lambda x: (-x[0], x[1])):
    for _ in range(x[0]):
        print(s[x[1]])