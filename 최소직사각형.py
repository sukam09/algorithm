from itertools import combinations

def solution(sizes):
    candidate = set()
    ans = float('inf')
    
    for w, h in sizes:
        candidate.add(w)
        candidate.add(h)
    
    if len(candidate) == 1:
        return list(candidate)[0] ** 2
    
    for a, b in combinations(candidate, 2):
        for w, h in sizes:
            if not ((w <= a and h <= b) or (w <= b and h <= a)):
                break
        else:
            ans = min(ans, a * b)
    
    return ans