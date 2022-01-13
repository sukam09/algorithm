from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())
a = Counter(map(int, input().split()))
v = int(input())
print(a[v])