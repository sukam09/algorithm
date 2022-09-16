import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve():
    for x in combinations(s, 6):
        print(*x)

while True:
    a = list(mis())
    k = a[0]
    s = a[1:]
    if k == 0:
        break
    solve()
    print()