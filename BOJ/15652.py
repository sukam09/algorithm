import itertools as it
input = __import__('sys').stdin.readline
N, M = map(int, input().split())
for p in it.combinations_with_replacement(range(1, N + 1), M): print(*p)