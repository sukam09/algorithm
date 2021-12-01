from collections import Counter

def solution(s):
    c = Counter(s.lower())
    return c['p'] == c['y']