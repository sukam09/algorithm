import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]
d[0][0] = 1
for i in range(n):
  for j in range(n):
    step = a[i][j]
    if step == 0:
      continue
    if i + step < n:
      d[i + step][j] += d[i][j]
    if j + step < n:
      d[i][j + step] += d[i][j]
print(d[-1][-1])