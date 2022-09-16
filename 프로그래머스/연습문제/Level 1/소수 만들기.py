from itertools import combinations

def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    ans = 0
    for c in combinations(nums, 3):
        if prime(sum(c)):
            ans += 1
    return ans