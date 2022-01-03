"""small case만 통과하는 code"""

from collections import deque

n = int(input())
m = int(input())
s = input()

p = lambda n: 'IO' * n + 'I'
pn = deque(p(n))
l = 2 * n + 1
q = deque(maxlen=l)
ans = 0

for c in s:
    q.append(c)
    if q == pn:
        ans += 1

print(ans)