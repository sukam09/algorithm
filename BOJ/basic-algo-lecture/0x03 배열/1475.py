from sys import stdin
from collections import defaultdict
from math import ceil
input = stdin.readline

n = input().rstrip()
a = defaultdict(int)
for c in n:
    if c == '9':
        a['6'] += 1
    else:
        a[c] += 1
a['6'] = ceil(a['6'] / 2)
print(max(a.values()))