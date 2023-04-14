import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]
for i in range(n):
    s[i] %= m
ans = 0
cnt = [0] * m
for i in range(n):
    cnt[s[i]] += 1
for i in range(m):
    ans += (cnt[i] * (cnt[i] - 1)) // 2
ans += cnt[0]
print(ans)