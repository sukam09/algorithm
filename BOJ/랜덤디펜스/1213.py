import sys
from collections import Counter
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
c = Counter(s)
odd_cnt = 0
odd_char = ''

for k, v in c.items():
    if v % 2 == 1:
        if odd_cnt == 1:
            print("I'm Sorry Hansoo")
            sys.exit(0)
        odd_cnt = 1
        odd_char = k

half = ''

for k, v in sorted(c.items()):
    half += k * (v // 2)

ans = half + odd_char + half[::-1]
print(ans)