from sys import stdin
from collections import Counter
input = stdin.readline

a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + 1000 * a)
elif a != b and b != c and c != a:
    print(100 * max(a, b, c))
else:
    print(1000 + Counter([a, b, c]).most_common(1)[0][0] * 100)