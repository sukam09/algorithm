from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().split()
    print("Possible" if Counter(a) == Counter(b) else "Impossible")