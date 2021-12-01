from math import sqrt


def dist(x, y):
    return sqrt(x ** 2 + y ** 2)

def solution(names, homes, grades):
    candidate = []
    rank = {}
    
    for name, home, grade in zip(names, homes, grades):
        candidate.append((int(grade), dist(home[0], home[1]), name))
    
    candidate.sort(key=lambda item: (-item[0], -item[1], item[2]))
    for i, c in enumerate(candidate):
        rank[c[2]] = i + 1
    
    ans = []
    for name in names:
        ans.append(rank[name])
    return ans