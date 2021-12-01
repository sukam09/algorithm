from itertools import permutations

def check(order, k, dungeons):
    cnt = 0
    
    for od in order:
        needed = dungeons[od][0]
        if k >= needed:
            k -= dungeons[od][1]
            cnt += 1
        else:
            return cnt
    
    return cnt

def solution(k, dungeons):
    n = len(dungeons)
    ans = 0
    
    for order in permutations(range(n), n):
        ans = max(ans, check(order, k, dungeons))
    
    return ans