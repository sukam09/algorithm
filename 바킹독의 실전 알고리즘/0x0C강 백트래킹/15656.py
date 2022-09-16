import sys
from itertools import product
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n, m = mis()
a = list(mis())
for x in product(sorted(a), repeat=m):
    print(*x)