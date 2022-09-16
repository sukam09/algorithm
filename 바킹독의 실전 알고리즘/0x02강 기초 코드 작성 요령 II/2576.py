from sys import stdin
input = stdin.readline

arr = [int(input()) for _ in range(7)]
odds = [x for x in arr if x % 2]
if not odds:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))