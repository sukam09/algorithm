from sys import stdin
from collections import Counter
input = stdin.readline

a = int(input())
b = int(input())
c = int(input())
res = a * b * c
cnt = Counter(map(int, list(str(res))))
for i in range(10):
    print(cnt[i])