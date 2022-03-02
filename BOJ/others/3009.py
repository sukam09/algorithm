import sys
from collections import Counter

xs, ys = [], []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)

xs, ys = Counter(xs), Counter(ys)
xs = dict(map(reversed, xs.items()))
ys = dict(map(reversed, ys.items()))
print(xs[1], ys[1])
