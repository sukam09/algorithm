import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for _ in range(n):
    url, pw = input().split()
    d[url] = pw
for _ in range(m):
    q = input().rstrip()
    print(d[q])