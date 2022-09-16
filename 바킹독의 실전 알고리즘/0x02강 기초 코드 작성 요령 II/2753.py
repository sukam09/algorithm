from sys import stdin
input = stdin.readline

n = int(input())
print(1 if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 else 0)