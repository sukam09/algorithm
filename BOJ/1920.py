import sys

N = int(sys.stdin.readline())
A = {x: 1 for x in list(map(int, sys.stdin.readline().split()))}
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
ans = [1 if x in A else 0 for x in B]
print('\n'.join(map(str, ans)))
