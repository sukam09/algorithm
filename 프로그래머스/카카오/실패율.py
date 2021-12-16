from collections import Counter

def solution(N, stages):
    res = []
    fail = Counter([s for s in stages if s <= N])
    for i in range(1, N + 1):
        challenger = len([s for s in stages if s >= i])
        res.append((fail[i] / challenger, i)) if challenger else res.append((0, i))
    res.sort(key=lambda item: (-item[0], item[1]))
    ans = [r[1] for r in res]
    return ans