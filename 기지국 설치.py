from math import ceil

def solution(n, stations, w):
    target = [0]
    W = 1 + 2 * w
    ans = 0
    
    for st in stations:
        target.append(max(st - w, 1))
        target.append(min(st + w, n))

    target.append(n + 1)

    for i in range(0, len(target) - 1, 2):
        ans += ceil((target[i + 1] - target[i] - 1) / W)

    return ans