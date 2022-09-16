import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n, m = mis()
a = list(mis())
for x in combinations(sorted(a), m):
    print(*x)