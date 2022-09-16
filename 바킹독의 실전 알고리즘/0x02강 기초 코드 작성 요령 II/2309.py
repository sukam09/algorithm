from sys import stdin
from itertools import combinations
input = stdin.readline

arr = [int(input()) for _ in range(9)]
tg = sum(arr) - 100
for cb in combinations(arr, 2):
    if sum(cb) == tg:
        ans = [x for x in arr if x not in cb]
        break

for x in sorted(ans):
    print(x)