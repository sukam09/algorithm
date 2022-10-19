import sys
input = sys.stdin.readline

def cal(cur, idx, i):
  if i == 0:
    return cur + num[idx]
  elif i == 1:
    return cur - num[idx]
  else:
    return cur * num[idx]

def dfs(cnt, cur):
  global mn, mx
  if cnt == n - 1:
    mn = min(mn, cur)
    mx = max(mx, cur)
    return
  for i in range(3):
    if op[i] == 0:
      continue
    op[i] -= 1
    dfs(cnt + 1, cal(cur, cnt + 1, i))
    op[i] += 1

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
mn = 1000000000
mx = -1000000000
dfs(0, num[0])
print(mn, mx)