from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
counter = Counter(cards)
m = int(input())
candidates = list(map(int, input().split()))
for candidate in candidates:
    print(counter[candidate], end=' ')