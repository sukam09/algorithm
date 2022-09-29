import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = Counter(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
for num in numbers:
    if num in cards:
        print(cards[num])
    else:
        print(0)