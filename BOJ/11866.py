import sys

N, K = map(int, sys.stdin.readline().split())
circle = {x: 1 for x in range(1, N + 1)}
idx = 0
ans = []

while circle != {}:
    keys = list(circle.keys())
    idx = (idx + K - 1) % len(keys)
    key = list(keys)[idx]
    ans.append(key)
    del circle[key]
print("<" + ', '.join(map(str, ans)) + ">")