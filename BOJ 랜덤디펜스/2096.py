# 메모리 제한이 4MB라 node.js로는 못푸는 문제
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * 3 for _ in range(n)]
d[0] = a[0]
for i in range(1, n):
  for j in range(3):
    mx = 0
    for k in [-1, 0, 1]:
      if 0 <= j + k < 3:
        mx = max(mx, d[i - 1][j + k])
    d[i][j] = mx + a[i][j]
ans1 = max(d[-1])
for i in range(1, n):
  for j in range(3):
    mn = float("inf")
    for k in [-1, 0, 1]:
      if 0 <= j + k < 3:
        mn = min(mn, d[i - 1][j + k])
    d[i][j] = mn + a[i][j]
ans2 = min(d[-1])
print(ans1, ans2)