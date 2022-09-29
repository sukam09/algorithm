import sys

n = list(map(int, sys.stdin.readline().split()))
if n == [1, 2, 3, 4, 5, 6, 7, 8]:
    ans = 'ascending'
elif n == [8, 7, 6, 5, 4, 3, 2, 1]:
    ans = 'descending'
else:
    ans = 'mixed'
print(ans)