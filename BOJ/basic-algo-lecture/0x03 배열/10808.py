from sys import stdin
from collections import Counter
input = stdin.readline

s = input()
cnt = Counter(s)
for c in 'abcdefghijklmnopqrstuvwxyz':
    print(cnt[c], end=' ')