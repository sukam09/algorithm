import sys
from collections import deque
input = sys.stdin.readline

def solve(n, d):
  order[n] = d
  if n - 1 >= 0 and order[n - 1] == 0 and board[n - 1][2] != board[n][6]:
    solve(n - 1, -d)
  if n + 1 < 4 and order[n + 1] == 0 and board[n][2] != board[n + 1][6]:
    solve(n + 1, -d)

board = list(deque(map(int, input().rstrip())) for _ in range(4))
k = int(input())
for _ in range(k):
  n, d = map(int, input().split())
  order = [0, 0, 0, 0]
  solve(n - 1, d)
  for i, x in enumerate(order):
    board[i].rotate(x)
s = list(board[i][0] for i in range(4))
print(s[0] + 2 * s[1] + 4 * s[2] + 8 * s[3])