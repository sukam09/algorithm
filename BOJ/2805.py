input = __import__('sys').stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
left, right = 0, max(tree) - 1
hmax = 0
while left <= right:
    mid = (left + right) // 2
    target = sum(t - mid for t in tree if t > mid)
    if target >= M:
        if mid > hmax: hmax = mid
        left = mid + 1
    else:
        right = mid - 1
print(hmax)