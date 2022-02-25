import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

d = [1] * 1005
pre = [-1] * 1005
ans = [0] * 1005

n = ii()
a = [0] + list(mis())
for i in range(2, n + 1):
    for j in range(1, i):
        if a[i] > a[j]:
            if d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                pre[i] = j
print(max(d))

mi = 1
md = d[1]
for i in range(2, n + 1):
    if d[i] > md:
        md = d[i]
        mi = i

cur = mi
idx = 0
while cur != -1:
    ans[idx] = a[cur]
    idx += 1
    cur = pre[cur]
for i in range(idx - 1, -1, -1):
    print(ans[i], end=' ')