from collections import Counter

a, b, c = map(int, input().split())
maxval = max(a, b, c)

if a == b == c:
    reward = 10000 + a * 1000
elif a != b and b != c and a != c:
    reward = maxval * 100
else:
    target = Counter([a, b, c]).most_common(1)[0][0]
    reward = 1000 + target * 100

print(reward)