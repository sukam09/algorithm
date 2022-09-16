from collections import Counter

def solution(scores):
    ans = ''
    n = len(scores)
    avg = []
    for j in range(n):
        res = []
        for i in range(n):
            res.append(scores[i][j])
        self = scores[j][j]
        total = sum(res)
        if (self == max(res) or self == min(res)) and Counter(res)[self] == 1:
            avg.append((total - self) / (n - 1))
        else:
            avg.append(total / n)
    for a in avg:
        if a >= 90:
            ans += 'A'
        elif a >= 80:
            ans += 'B'
        elif a >= 70:
            ans += 'C'
        elif a >= 50:
            ans += 'D'
        else:
            ans += 'F'
    return ans