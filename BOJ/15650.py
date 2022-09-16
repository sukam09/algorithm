import itertools as it
input = __import__('sys').stdin.readline
N, M = map(int, input().split())
for c in it.combinations(range(1, N + 1), M): print(*c)