from sys import stdin
from collections import Counter
input = stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
cnt1 = Counter(s1)
cnt2 = Counter(s2)
ans = 0
for c in 'abcdefghijklmnopqrstuvwxyz':
    ans += max(cnt1[c], cnt2[c]) - min(cnt1[c], cnt2[c])
print(ans)