from math import factorial

def solution(n, k):
    cand = list(range(1, n + 1))
    n, k = n - 1, k - 1
    ans = []
    
    while cand:
        category, idx = divmod(k, factorial(n))
        ans.append(cand.pop(category))
        n -= 1
        k = idx
    
    return ans