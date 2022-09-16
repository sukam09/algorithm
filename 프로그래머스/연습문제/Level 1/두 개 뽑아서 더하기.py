from itertools import combinations

def solution(numbers):
    ans = []
    for c in combinations(numbers, 2):
        ans.append(sum(c))
    return sorted(set(ans))