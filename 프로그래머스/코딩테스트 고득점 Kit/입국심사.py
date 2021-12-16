def solution(n, times):
    left, right = 1, max(times) * n
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                break
        
        if cnt < n:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    
    return ans