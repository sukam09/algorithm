h, w = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(w):
    if i == 0 or i == w - 1:
        continue
    height = min(max(arr[:i]), max(arr[i + 1:]))
    if height >= arr[i]:
        ans += height - arr[i]

print(ans)