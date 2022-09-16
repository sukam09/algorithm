import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
c = list(combinations(cards, 3))
c = [sum(x) for x in c if sum(x) <= M]
print(max(c))
