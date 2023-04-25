from math import ceil
from heapq import heappush, heappop

def find_median(arr):
    left = []
    right = []
    mid = arr[0]
    ans = [mid]
    
    for i in range(1, len(arr)):
        val = arr[i]
        heappush(right, val) if val > mid else heappush(left, -val)
        if i % 2 == 0:
            if len(left) < len(right):
                heappush(left, -mid)
                mid = heappop(right)
            elif len(left) > len(right):
                heappush(right, mid)
                mid = -heappop(left)
            ans.append(mid)
    
    return ans

t = int(input())
for _ in range(t):
    m = int(input())
    arr = []
    
    for _ in range(ceil(m / 10)):
        numbers = list(map(int, input().split()))
        arr.extend(numbers)
    
    print(m // 2 + 1)
    ans = find_median(arr)
    for i, val in enumerate(ans):
        if i and not i % 10:
            print()
        print(val, end=' ')