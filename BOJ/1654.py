input = __import__('sys').stdin.readline
K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]
left, right = 1, max(L)
maxval = 0
while left <= right:
    mid = (left + right) // 2
    target = sum(i // mid for i in L)
    if target >= N:
        if mid > maxval: maxval = mid
        left = mid + 1
    else:
        right = mid - 1
print(maxval)