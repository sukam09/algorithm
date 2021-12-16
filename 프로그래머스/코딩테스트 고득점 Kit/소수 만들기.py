from itertools import combinations
from math import sqrt

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    ans = 0
    c = combinations(nums, 3)
    for x in c:
        if prime(sum(x)):
            ans += 1
    return ans