def bitonic(arr):
    target = -1
    maxval = max(arr)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return False
        if arr[i] == maxval:
            if target == -1:
                target = i
            else:
                return False

    left, right = arr[:target], arr[target + 1:]
    
    if len(left) == 0 or len(right) == 0:
        return False
    
    return sorted(left) == left and sorted(right, reverse=True) == right

def solution(arr):
    n = len(arr)
    ans = 0
    for i in range(3, n + 1):
        for j in range(n - i + 1):
            p = arr[j:j + i]
            if bitonic(p):
                print(p)
                ans += 1
    
    return ans % (10 ** 9 + 7)