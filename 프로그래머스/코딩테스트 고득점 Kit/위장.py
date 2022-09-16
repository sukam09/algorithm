from collections import defaultdict

def solution(clothes):
    dic = defaultdict(list)
    for v, k in clothes:
        dic[k].append(v)
    ans = 1
    for k in dic:
        ans *= len(dic[k]) + 1
    return ans - 1