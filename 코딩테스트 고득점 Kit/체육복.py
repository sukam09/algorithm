from collections import defaultdict

def solution(n, lost, reserve):
    lr = set(lost) & set(reserve)
    lost = list(set(lost) - lr)
    reserve = list(set(reserve) - lr)
    rdic = defaultdict(bool)
    ans = n - len(lost)
    for x in reserve:
        rdic[x] = True
    for x in lost:
        if rdic[x - 1]:
            ans += 1
            rdic[x - 1] = False
        elif rdic[x + 1]:
            ans += 1
            rdic[x + 1] = False
    return ans