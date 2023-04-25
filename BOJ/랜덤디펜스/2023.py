# node.js로 못푸는 문제 (MLE)
import sys
input = sys.stdin.readline

def isprime(n):
  if n == 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def dfs(x, cur):
  if x == n:
    print(cur)
    return
  for i in range(1, 10):
    nxt = cur * 10 + i
    if isprime(nxt):
      dfs(x + 1, nxt)

n = int(input())
dfs(0, 0)