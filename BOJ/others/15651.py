import itertools as it
input = __import__('sys').stdin.readline
N, M = map(int, input().split())
for p in it.product(range(1, N + 1), repeat=M): print(*p)