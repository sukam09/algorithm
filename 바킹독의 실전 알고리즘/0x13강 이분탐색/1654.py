from sys import stdin
input = stdin.readline

k, n = map(int, input().split())
lines = list(int(input()) for _ in range(k))
left, right = 1, max(lines)
ans = 0

while left <= right:
    mid = (left + right) // 2
    cnt = sum(line // mid for line in lines)
    if cnt < n:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)