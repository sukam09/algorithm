from sys import stdin
input = stdin.readline

arr = sorted(map(int, input().split()))
print(*arr)