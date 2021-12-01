from math import floor, sqrt

def solution(n):
    x = floor((-1 + sqrt(1 + 8 * n)) / 2)
    ans = 0

    for i in range(1, x + 1):
        start = 1
        s = 0
        while s <= n:
            s = sum(range(start, start + i))
            if s == n:
                ans += 1
                break
            start += 1
    
    return ans