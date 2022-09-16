from sys import stdin
input = stdin.readline

cnt = int(input())
divisors = sorted(list(map(int, input().split())))
print(min(divisors) * max(divisors))