import sys

n = list(map(int, sys.stdin.readline().split()))
n = [x ** 2 for x in n]
print(sum(n) % 10)