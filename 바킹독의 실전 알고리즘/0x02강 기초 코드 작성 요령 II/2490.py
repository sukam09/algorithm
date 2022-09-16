from sys import stdin
input = stdin.readline

s = 'EABCD'
for _ in range(3):
    print(s[list(map(int, input().split())).count(0)])