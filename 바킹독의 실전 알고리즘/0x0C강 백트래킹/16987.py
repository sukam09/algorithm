import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve(idx):
    global ans, cnt
    if idx == n:
        ans = max(ans, cnt)
        return

    cur = a[idx]
    if cur[0] <= 0 or cnt == n - 1:
        solve(idx + 1)
        return
    for i in range(n):
        tg = a[i]
        if i == idx or tg[0] <= 0:
            continue
        cur[0] -= tg[1]
        tg[0] -= cur[1]
        if cur[0] <= 0:
            cnt += 1
        if tg[0] <= 0:
            cnt += 1
        solve(idx + 1)
        if cur[0] <= 0:
            cnt -= 1
        if tg[0] <= 0:
            cnt -= 1
        cur[0] += tg[1]
        tg[0] += cur[1]

n = ii()
a = [list(mis()) for _ in range(n)]
ans = 0
cnt = 0
solve(0)
print(ans)