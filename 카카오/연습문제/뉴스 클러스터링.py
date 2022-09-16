from collections import Counter

def solution(str1, str2):
    set1 = [(f + s).lower() for f, s in zip(str1, str1[1:]) if (f + s).isalpha()]
    set2 = [(f + s).lower() for f, s in zip(str2, str2[1:]) if (f + s).isalpha()]
    if not set1 and not set2:
        return 65536
    candidate = set(set1) | set(set2)
    c1, c2 = Counter(set1), Counter(set2)
    intersection, union = 0, 0
    for c in candidate:
        intersection += min(c1[c], c2[c])
        union += max(c1[c], c2[c])
    jaccard = intersection / union
    return int(jaccard * 65536)