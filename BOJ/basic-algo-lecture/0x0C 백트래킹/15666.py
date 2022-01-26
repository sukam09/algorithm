import sys
from itertools import combinations_with_replacement
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n, m = mis()
a = list(mis())
ans = set(x for x in combinations_with_replacement(sorted(a), m))
for x in sorted(ans):
    print(*x)