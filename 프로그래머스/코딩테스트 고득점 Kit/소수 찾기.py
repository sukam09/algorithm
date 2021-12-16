from itertools import permutations
from math import sqrt
from collections import defaultdict

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    prime = defaultdict(int)
    ans = 0
    for i in range(1, len(numbers)+1):
        p = permutations(numbers, i)
        for x in p:
            res = int(''.join(list(x)))
            if isprime(res) and prime[res] == 0:
                ans += 1
                prime[res] += 1
    return ans