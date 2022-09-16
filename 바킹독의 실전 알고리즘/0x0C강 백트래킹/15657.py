import sys
from itertools import combinations_with_replacement
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n, m = mis()
a = list(mis())
for x in combinations_with_replacement(sorted(a), m):
    print(*x)