import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

cnt = [0, 0]
s = input()
cur = '2'
for c in s:
    if c != cur:
        cur = c
        cnt[int(c)] += 1
print(min(cnt))