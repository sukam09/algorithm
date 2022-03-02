input = __import__('sys').stdin.readline
N, M = map(int, input().split())
from itertools import permutations
ans = permutations(range(1, N + 1), M)
for x in ans: print(*x)