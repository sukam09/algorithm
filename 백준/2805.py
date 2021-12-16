n, m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 1, max(trees)
ans = 0

while left <= right:
    mid = (left + right) // 2
    cutted_trees = sum(tree - mid if tree >= mid else 0 for tree in trees)
    if cutted_trees < m:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)