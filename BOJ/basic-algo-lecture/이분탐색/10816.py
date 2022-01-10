from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())
cards = list(map(int, input().split()))
counter = Counter(cards)
m = int(input())
candidates = list(map(int, input().split()))
for candidate in candidates:
    print(counter[candidate], end=' ')