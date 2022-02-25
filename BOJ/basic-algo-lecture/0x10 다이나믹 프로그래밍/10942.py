import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve():
    for i in range(1, n + 1): d[i][i] = 1
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            if a[i] == a[j]:
                if j == i + 1: d[i][j] = 1
                elif d[i + 1][j - 1]: d[i][j] = 1

n = ii()
a = [0] + list(mis())
m = ii()
d = [[0] * 2005 for _ in range(2005)]
solve()
for _ in range(m):
    s, e = mis()
    print(d[s][e])