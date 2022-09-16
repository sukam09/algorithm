import sys
from collections import deque

N = int(sys.stdin.readline())
cards = deque([x for x in range(1, N + 1)])
while True:
    if len(cards) > 2:
        cards.popleft()
        cards.rotate(-1)
    elif len(cards) == 2:
        cards.popleft()
        print(cards[0])
        break
    else:
        # only one card exists
        print(cards[0])
        break
