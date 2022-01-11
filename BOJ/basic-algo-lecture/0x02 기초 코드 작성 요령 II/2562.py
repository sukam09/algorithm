from sys import stdin
input = stdin.readline

arr = [int(input()) for _ in range(9)]
print(max(arr))
print(arr.index(max(arr)) + 1)