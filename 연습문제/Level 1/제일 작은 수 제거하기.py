def solution(arr):
    if len(arr) == 1:
        return [-1]
    minval = float('inf')
    for i, val in enumerate(arr):
        if val < minval:
            minval = val
            target = i
    return arr[:target] + arr[target + 1:]