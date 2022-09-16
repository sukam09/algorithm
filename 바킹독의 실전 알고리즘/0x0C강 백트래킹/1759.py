import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

l, c = mis()
v = 'aeiou'
a = input().split()
ans = []
for x in combinations(a, l):
    cnt = 0
    for y in x:
        if y in v:
            cnt += 1
    if cnt >= 1 and l - cnt >= 2:
        ans.append(sorted(x))
for x in sorted(ans):
    print(*x, sep='')