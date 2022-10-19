import sys
input = sys.stdin.readline

# 오, 왼, 위, 아
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def OOB(x, y):
  return x < 0 or x >= n or y < 0 or y >= n

def rev(d):
  nd = [1, 0, 3, 2]
  return nd[d]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
status = [[[] for _ in range(n)] for _ in range(n)]
marker = []
for i in range(k):
  x, y, d = map(int, input().split())
  x -= 1
  y -= 1
  d -= 1
  marker.append([x, y, d])
  status[x][y].append(i)
ans = 1
while ans <= 1000:
  for i in range(k):
    re = False
    while True:
      x, y, d = marker[i]
      idx = status[x][y].index(i)
      l = len(status[x][y])
      nx = x + dx[d]
      ny = y + dy[d]
      if OOB(nx, ny) or board[nx][ny] == 2:
        if not re:
          d = rev(d)
          marker[i][2] = d
          nx = x + dx[d]
          ny = y + dy[d]
          re = True
          continue
        else:
          break
      elif board[nx][ny] == 1:
        status[x][y][idx:] = reversed(status[x][y][idx:])
      for j in range(idx, l):
        cur = status[x][y][j]
        status[nx][ny].append(cur)
        marker[cur][0] = nx
        marker[cur][1] = ny
      for j in range(idx, l):
        status[x][y].pop()
      if len(status[nx][ny]) >= 4:
        print(ans)
        sys.exit(0)
      break
  ans += 1
print(-1)