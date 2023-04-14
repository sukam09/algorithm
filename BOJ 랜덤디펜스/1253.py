import sys
input = sys.stdin.readline

def solve(x):
    global ans
    tmp = a[:x] + a[x + 1:]
    st = 0
    en = len(tmp) - 1
    while st < en:
        if tmp[st] + tmp[en] == a[x]:
            ans += 1
            return
        if tmp[st] + tmp[en] < a[x]: st += 1
        else: en -= 1

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    solve(i)
print(ans)