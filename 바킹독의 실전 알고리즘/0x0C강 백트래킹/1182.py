import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

n, s = mis()
a = list(mis())
ans = 0
for i in range(1, n + 1):
    for x in combinations(a, i):
        if sum(x) == s:
            ans += 1
print(ans)